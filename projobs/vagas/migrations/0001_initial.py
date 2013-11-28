# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vaga'
        db.create_table(u'vagas_vaga', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresas.Empresa'])),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('setor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('inicio', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('quantidade', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'vagas', ['Vaga'])

        # Adding M2M table for field requisitos on 'Vaga'
        m2m_table_name = db.shorten_name(u'vagas_vaga_requisitos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vaga', models.ForeignKey(orm[u'vagas.vaga'], null=False)),
            ('requisito', models.ForeignKey(orm[u'vagas.requisito'], null=False))
        ))
        db.create_unique(m2m_table_name, ['vaga_id', 'requisito_id'])

        # Adding model 'ProcessoSeletivo'
        db.create_table(u'vagas_processoseletivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vaga', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vagas.Vaga'])),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'vagas', ['ProcessoSeletivo'])

        # Adding model 'Inscricao'
        db.create_table(u'vagas_inscricao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('processo_seletivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vagas.ProcessoSeletivo'])),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('data', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('pretensao_salarial', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nota_escrita', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_dinamica', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_curriculo', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'vagas', ['Inscricao'])

        # Adding M2M table for field requisitos on 'Inscricao'
        m2m_table_name = db.shorten_name(u'vagas_inscricao_requisitos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inscricao', models.ForeignKey(orm[u'vagas.inscricao'], null=False)),
            ('requisito', models.ForeignKey(orm[u'vagas.requisito'], null=False))
        ))
        db.create_unique(m2m_table_name, ['inscricao_id', 'requisito_id'])

        # Adding model 'Entrevista'
        db.create_table(u'vagas_entrevista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inscricao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vagas.Inscricao'])),
            ('relatorio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'vagas', ['Entrevista'])

        # Adding model 'Requisito'
        db.create_table(u'vagas_requisito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requisito', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'vagas', ['Requisito'])


    def backwards(self, orm):
        # Deleting model 'Vaga'
        db.delete_table(u'vagas_vaga')

        # Removing M2M table for field requisitos on 'Vaga'
        db.delete_table(db.shorten_name(u'vagas_vaga_requisitos'))

        # Deleting model 'ProcessoSeletivo'
        db.delete_table(u'vagas_processoseletivo')

        # Deleting model 'Inscricao'
        db.delete_table(u'vagas_inscricao')

        # Removing M2M table for field requisitos on 'Inscricao'
        db.delete_table(db.shorten_name(u'vagas_inscricao_requisitos'))

        # Deleting model 'Entrevista'
        db.delete_table(u'vagas_entrevista')

        # Deleting model 'Requisito'
        db.delete_table(u'vagas_requisito')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'logradouro': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'empresas.empresa': {
            'Meta': {'object_name': 'Empresa', '_ormbases': [u'accounts.User']},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'profissionais.profissional': {
            'Meta': {'object_name': 'Profissional', '_ormbases': [u'accounts.User']},
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'vagas.entrevista': {
            'Meta': {'object_name': 'Entrevista'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscricao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vagas.Inscricao']"}),
            'relatorio': ('django.db.models.fields.TextField', [], {})
        },
        u'vagas.inscricao': {
            'Meta': {'object_name': 'Inscricao'},
            'data': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota_curriculo': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_dinamica': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_escrita': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pretensao_salarial': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'processo_seletivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vagas.ProcessoSeletivo']"}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"}),
            'requisitos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['vagas.Requisito']", 'symmetrical': 'False'})
        },
        u'vagas.processoseletivo': {
            'Meta': {'object_name': 'ProcessoSeletivo'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profissionais': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profissionais.Profissional']", 'through': u"orm['vagas.Inscricao']", 'symmetrical': 'False'}),
            'vaga': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vagas.Vaga']"})
        },
        u'vagas.requisito': {
            'Meta': {'object_name': 'Requisito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requisito': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'vagas.vaga': {
            'Meta': {'object_name': 'Vaga'},
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empresas.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quantidade': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'requisitos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vagas.Requisito']", 'null': 'True', 'blank': 'True'}),
            'setor': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['vagas']