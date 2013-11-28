# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profissional'
        db.create_table(u'profissionais_profissional', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')()),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['Profissional'])

        # Adding model 'FormacaoProfissional'
        db.create_table(u'profissionais_formacaoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('empresa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('inicio', self.gf('django.db.models.fields.DateField')()),
            ('termino', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('atual', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'profissionais', ['FormacaoProfissional'])

        # Adding model 'FormacaoAcademica'
        db.create_table(u'profissionais_formacaoacademica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('curso', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data_conclusao', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['FormacaoAcademica'])


    def backwards(self, orm):
        # Deleting model 'Profissional'
        db.delete_table(u'profissionais_profissional')

        # Deleting model 'FormacaoProfissional'
        db.delete_table(u'profissionais_formacaoprofissional')

        # Deleting model 'FormacaoAcademica'
        db.delete_table(u'profissionais_formacaoacademica')


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
        u'profissionais.formacaoacademica': {
            'Meta': {'object_name': 'FormacaoAcademica'},
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'curso': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'data_conclusao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"})
        },
        u'profissionais.formacaoprofissional': {
            'Meta': {'object_name': 'FormacaoProfissional'},
            'atual': ('django.db.models.fields.BooleanField', [], {}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"}),
            'termino': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'profissionais.profissional': {
            'Meta': {'object_name': 'Profissional', '_ormbases': [u'accounts.User']},
            'cpf': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['profissionais']