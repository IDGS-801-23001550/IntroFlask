from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, FloatField, RadioField
from wtforms import EmailField
from wtforms import validators
from wtforms.validators import DataRequired, NumberRange

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese nombre valido")
    ])
    apaterno = StringField("Apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno = StringField("Amaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo", [
        validators.Email(message="Ingresa correo valido")
    ])

class UserFormc(Form):
    nombre = StringField(
        'Nombre',
        validators=[DataRequired(message="El campo es requerido")]
    )

    compradores = IntegerField(
        'Cantidad de compradores',
        validators=[
            DataRequired(message="El campo es requerido"),
            NumberRange(min=1, message="Debe haber al menos 1 comprador")
        ]
    )

    cantidad = IntegerField(
        'Cantidad de boletos',
        validators=[
            DataRequired(message="El campo es requerido"),
            NumberRange(min=1, message="Cantidad inválida")
        ]
    )

    cineco = RadioField(
        'Cineco',
        validators=[DataRequired(message="Seleccione una opción")],
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no'
    )