from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from django.core.mail import EmailMessage
from django.db import transaction
from django.template.loader import render_to_string
from django.conf import settings
from core.celery import app


@app.task
def send_message(main, products):
    try:
        # Указываем путь к файлу шрифта и его имя
        font_path = r'utils\d9464-arkhip_font.ttf'
        font_name = 'd9464-arkhip_font.ttf'

        cashier = f'{main.name}'

        products = products

        doc = SimpleDocTemplate(r"media\checks\{}__check.pdf".format(main.id) , pagesize=letter)
        # Регистрируем шрифт
        pdfmetrics.registerFont(TTFont(font_name, font_path))

        # Создаем стиль с использованием вашего шрифта
        custom_style = ParagraphStyle(
            'custom_style',
            parent=getSampleStyleSheet()['Normal'],
            fontName=font_name,
            fontSize=12,
            textColor=colors.black,
            spaceAfter=12,
            alignment=1
        )

        content = []

        content.append(Paragraph('*' * 75, custom_style))
        content.append(Paragraph('\t\tRECEIPT, AMWAY', custom_style))
        content.append(Paragraph('\t\t+(996)123456', custom_style))
        content.append(Paragraph('=' * 49, custom_style))
        content.append(Paragraph(f'Cashier: {cashier}', custom_style))

        date = str(datetime.now())[:10]
        time = str(datetime.now())[10:][:6]
        content.append(Paragraph(f'{date: >29}        {time: >19}', custom_style))
        content.append(Paragraph('=' * 49, custom_style))
        content.append(Paragraph('GROCERY', custom_style))

        for k in products.all():
            price = k.product.price*k.quantity
            content.append(Paragraph(f'{k.order.name:.<39}({k.quantity})<font color="blue" size="10">{price: >9}</font>', custom_style))

        content.append(Paragraph('=' * 49, custom_style))
        Total = [i.product.price * i.quantity for i in products]
        res= f'Total: {"=" + str(sum(Total))}'
        content.append(Paragraph(res, custom_style))

        doc.build(content)


        subject = 'New order!'
        email = EmailMessage(subject, '', 'ssavutokhunov@gmail.com', ['zalalidinovroma@gmail.com',main.gmail])
        email.attach_file(r"media\checks\{}__check.pdf".format(main.id))
        email.send()
        
    except Exception as ex:
        print(ex)


@app.task
def send_message_about_consultation(instance):
    try:
        send_mail('New person for consultation!', 
                f'ФИО: {instance.name} \nНомер телефона: {instance.phone_number} \nПочта: {instance.gmail}', 
                'ssavutokhunov@gmail.com',
                ['zalalidinovroma@gmail.com'], 
                fail_silently=False)
    except Exception as ex:
        print(ex)



