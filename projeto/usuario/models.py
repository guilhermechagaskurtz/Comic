from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from utils.gerador_hash import gerar_hash

class AdministradorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='ADMINISTRADOR', is_active=True)


class ProfessorAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='PROFESSOR', is_active=True)


class BolsistaAtivoManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo='BOLSISTA', is_active=True)


class Usuario(AbstractBaseUser):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS = (
        ('ADMINISTRADOR', 'Administrador'),
        ('PROFESSOR', 'Professor' )
    )

    AREAS = (
        ('CIÊNCIAS DA SAÚDE', 'Ciências da Saúde'),
        ('CIÊNCIAS HUMANAS', 'Ciências Humanas' ),
        ('CIÊNCIAS SOCIAIS', 'Ciências Sociais'),
        ('CIÊNCIAS TECNOLÓGICAS', 'Ciências Tecnológicas' ),
    )

    USERNAME_FIELD = 'email'

    tipo = models.CharField(_(u'Tipo do usuário'),null=False, blank=False, max_length=15, choices=TIPOS, default='PROFESSOR')
    nome = models.CharField(_(u'Nome *'),null=False, blank=False, max_length=100, help_text='Campo obrigatório como todos os que tiverem *')
    email = models.EmailField(_('Email *'),null=False, blank=False, unique=True, max_length=100, db_index=True)
    data_nasc = models.DateField(_(u'Data de Nascimento'), blank = True , null = True, help_text='dd/mm/aaaa')
    cpf = models.CharField(_('CPF'),max_length=14, help_text='Atenção: SOMENTE OS NÚMEROS')
    rg = models.CharField(_('RG'), max_length=14, help_text='Atenção: SOMENTE OS NÚMEROS')
    matricula = models.CharField(_('Matrícula'),max_length=10,blank=True, null=True)
    lattes = models.CharField(_('Lattes *'), help_text="Clique <a href='http://buscatextual.cnpq.br/buscatextual' target='_blank'> aqui </a> para descobrir", max_length = 100)
    instituicao = models.ForeignKey('instituicao.Instituicao', verbose_name="Instituição", null=True, blank=True, on_delete=models.PROTECT)
    area_conhecimento_cnpq =  models.CharField(_(u'Área de conhecimento *'),max_length=50,choices=AREAS)
    curso_graduacao_vinculado = models.CharField(_('Curso de graduação vinculado *'),null=False, blank=False,help_text='Nome do curso que está lotado',max_length=50)
    curso_pos_graduacao = models.CharField(_('Curso de pós-graduação vinculado'),null=True,blank=True,max_length=50)
    grupo_pesquisa = models.CharField(_('Grupo de pesquisa vinculado'),null=True,blank=True,max_length=50)
    is_active = models.BooleanField(_(u'Ativo'), default=True, help_text='Se ativo o usuário tem permissão para acessar o sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = UserManager()
    administradores = AdministradorAtivoManager()
    professores = ProfessorAtivoManager()
    bolsistas = BolsistaAtivoManager()

    class Meta:
        ordering            =   [u'nome']
        verbose_name        =   _(u'usuário')
        verbose_name_plural =   _(u'usuários')

    def __str__(self):
        return self.nome
    
    def get_id(self):
        return self.id

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    @property
    def get_first_name(self):
        nomes = self.nome.split()
        return nomes[0]

    def get_short_name(self):
        return self.nome[0:10].strip()

    def get_full_name(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.nome = self.nome.upper()
        if not self.id:
            self.set_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        if self.tipo == 'ADMINISTRADOR':
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse('usuario_update', args=[str(self.id)])

    @property
    def get_usuario_register_activate_url(self):
        return '%s%s' % (settings.DOMINIO_URL, reverse('usuario_register_activate', kwargs={'slug': self.slug}))

    @property
    def get_delete_url(self):
        return reverse('usuario_delete', args=[str(self.id)])


