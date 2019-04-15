from django.db import models

# Create your models here.

class Mp(models.Model):

    Nombre = models.CharField(max_length=50, help_text='Nombre Completo empezando por Nombre, Apellido Paterno, Apellido Materno')
    Cargo = models.CharField(max_length=50,help_text='Ingrese el cargo de la Autoridad')
    Adscripcion = models.CharField(max_length=100, help_text='Ingrese el lugar de Agencia o Unidad')
    class Meta:
        ordering = ['Nombre']
        verbose_name = "Autoridad"
        verbose_name_plural= "Autoridades"
    def __str__(self):
      return '%s' % (self.Nombre)

class Expediente(models.Model):
    Num_Ingreso = models.AutoField(primary_key = True)
    Cantidad_de_Indicios = models.IntegerField(default=1)
    Lugar_de_Resguardo = (('B','Bóveda'),
                          ('A', 'Bodega de Bienes Asegurados'),
                          )
    Resguardo_en = models.CharField(max_length = 1, choices = Lugar_de_Resguardo, default = 'B' )
    Carpeta_Investigacion = models.CharField(max_length = 100, help_text = 'Ingrese el numero de Carpeta de Investigación')

    Titular = models.ForeignKey('Mp',on_delete = models.SET_NULL, null = True)

    Fecha_Ingreso = models.DateField(null=True, blank=True)

    Hora_Ingreso = models.TimeField(null=True, blank=True)

    Oficio = models.CharField(max_length=15)

    class Meta:
        
        verbose_name = "Carpeta"
    def __str__(self):
      return '(%s) %s' %(self.Num_Ingreso, self.Carpeta_Investigacion)

class Indicio(models.Model):
    # campo para llevar el control de ingresos por carpeta
    Ingreso_Num = models.ForeignKey('Expediente', on_delete= models.SET_NULL, null=True)

    ##Expediente = models.ForeignKey('Ingresos', on_delete = models.SET_NULL, null = True)
    # Expediente = models.CharField(max_length=100, help_text = 'Ingrese el Numero de Carpeta')


    No_Indicio = models.CharField(max_length=10, help_text='Ingrese el numero de indicio')

    tipo_indicio = (('F', 'Físico'),
                    ('O', 'Orgánico'),
                    ('B', 'Biológico'),
                    ('FO', 'Físico/Orgánico')
                    )

    Tipo = models.CharField(max_length=2, choices=tipo_indicio, default='F')

    Descripcion = models.TextField(max_length=500, help_text='Describe el indicio como la etiqueta')

    Rue = models.CharField(max_length=15, help_text='Formato = OM/F/100/2019',)

    clase_indicio = (
        ('AC', 'Arma de Fuego Corta'),
        ('AF', 'Arma de Fuego Larga'),
        ('PP', 'Pistola de Plastico'),
        ('AB', 'Arma Blanca'),
        ('EM', 'Estupefaciente-Marihuana'),
        ('EC', 'Estupefaciente-Cocaína'),
        ('EH', 'Estupefaciente-Heroína'),
        ('EA', 'Estupefaciente-Anfetamina'),
        ('ER', 'Estupefaciente-Cristal'),
        ('EL', 'Estupefaciente-LCD'),
        ('T', 'Tabaco'),
        ('AL', 'Alcohol'),
        ('P', 'Perecedero'),
        ('E', 'Electrónico'),
        ('AP', 'Autopartes'),
        ('H', 'Herramientas'),
        ('AR', ' Artículos de Belleza'),
        ('J', 'Joyeria'),
        ('R', ' Ropa'),
        ('N', ' Numerario'),
        ('DC', 'Documentos'),
        ('MA', 'Medio de Almacenamiento'),
        ('M', 'Medicamento'),
        ('EB', 'Elemento Balístico'),
        ('O', 'Otro'),
    )

    Clasificacion = models.CharField(max_length=2, choices=clase_indicio, default='A')

    Fecha_Caducidad = models.DateField(null=True, blank=True)

    Peso_Narcotico = models.FloatField(default= 0.000)


    dictamen_sino = (('S', 'Si'),
                    ('N', 'No'),
                    )

    Dictamen = models.CharField(max_length=1,choices=dictamen_sino,default='S')

    Si_No = (('S', 'Si'),
             ('N', 'No'),
             )
    Deposito_Banco = models.CharField(max_length=1, choices=Si_No, default='N')
    Cantidad = models.FloatField(default=0.00)

    Persona_Entrega = models.CharField(max_length=50, help_text='Ingrese Nombre de quien entrega fisicamente el indicio')

    sicadena = (('S', 'Si'),
                ('N', 'No'),
                ('CS', 'Copia Simple'),
                ('CC', 'Copia Certificada'),
                )

    Cadena = models.CharField(max_length=2, choices=sicadena, default='S')

    tipo_embalaje = (('B', 'Bolsa de Plástico'),
                     ('BP', 'Bolsa de Papel'),
                     ('SB', 'Sobre Blanco'),
                     ('SM', 'Sobre Manila'),
                     ('EM', 'Emplayado'),
                     ('CJ', 'Caja de Cartón'),
                     ('SE', 'Sin Embalaje'),
                     ('O', 'Otro'),
                     )
    Embalaje = models.CharField(max_length=2, choices=tipo_embalaje, default="B")
    edo_ambalaje = (('C', 'Cerrado'),
                    ('A', 'Abierto'),
                    ('AL', 'Alterado'),
                    ('R', 'Roto'),
                    ('O', 'Otro')
                    )

    Estado_embalaje = models.CharField(max_length=2, choices=edo_ambalaje, default="C")

    Ubicacion = models.CharField(max_length=50, help_text='Ingrese ubicacion del indicio')
    Imagen = models.ImageField(upload_to="userlogo/", blank=True, null=True)

    # crear una tabla para definir el estatus del indicio

    Observaciones = models.TextField(max_length=200,
                                     help_text='Aqui puede hacer observaciones del indicio y embalaje, entre otras',null = True, blank = True)


    class Meta:
        verbose_name = "Ingreso"
    #class Admin:
    #    list_display = ('Rue','Descripcion''Clasificacion')
    #    list_filter = ('Descripcion', 'Rue')
    #    ordering = ('Rue',)
    #    search_fields = ('Rue',)

    def __str__(self):
       return '(%s) %s' % (self.id, self.Rue)

class Rue(models.Model):
    ultimo_rue = models.IntegerField(default=530)


    def __str__(self):
        return '%s' %(self.ultimo_rue)

    def nuevo_rue(self):
        total = Rue.ultimo_rue + 1
        return total

class Definitiva(models.Model):
    Carpeta = models.ForeignKey('Expediente', on_delete = models.SET_NULL, null = True)
    Rue = models.OneToOneField('Indicio', on_delete = models.SET_NULL, null=True)
    Fecha_de_Movimiento = models.DateField(null=True, blank=True)
    Autoridad = models.ForeignKey('Mp', on_delete = models.SET_NULL, null = True)
    Persona_Recibe = models.CharField(max_length=50, help_text='Ingrese Nombre de quien recibe fisicamente el indicio')
    Imagen_salida = models.ImageField(upload_to="definitiva/", blank=True, null=True)
    Oficio = models.CharField(max_length = 20, help_text= 'Ingrese el número de Oficio',blank= True,null=True)
    Sasca =  models.CharField(max_length = 10, help_text = 'Ingrese el número de Sasca',blank= True,null=True)

    def __str__(self):
        return '%s' %(self.Rue)

class Temporal(models.Model):
    Carpeta = models.ForeignKey('Expediente', on_delete = models.SET_NULL, null = True)
    Rue = models.OneToOneField('Indicio', on_delete = models.SET_NULL, null=True)
    Fecha_de_Movimiento = models.DateField(null=True, blank=True)
    Autoridad = models.ForeignKey('Mp', on_delete = models.SET_NULL, null = True)
    Persona_Recibe = models.CharField(max_length=50, help_text='Ingrese Nombre de quien recibe fisicamente el indicio')
    Imagen_salida = models.ImageField(upload_to="temporal/", blank=True, null=True)

    def __str__(self):
        return '%s' %(self.Rue)

class Traslado(models.Model):
    Carpeta = models.ForeignKey('Expediente', on_delete = models.SET_NULL, null = True)
    Rue = models.OneToOneField('Indicio', on_delete = models.SET_NULL, null=True)
    Fecha_de_Movimiento = models.DateField(null=True, blank=True)
    Autoridad = models.ForeignKey('Mp', on_delete = models.SET_NULL, null = True)
    Persona_Recibe = models.CharField(max_length=50, help_text='Ingrese Nombre de quien recibe fisicamente el indicio')
    Imagen_salida = models.ImageField(upload_to="traslado/", blank=True, null=True)

    
    def __str__(self):
      return '%s %s' % (self.Rue, self.Fecha_de_Movimiento)





