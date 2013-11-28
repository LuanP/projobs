# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Inscricao.situacao'
        db.add_column(u'vagas_inscricao', 'situacao',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding unique constraint on 'Inscricao', fields ['profissional', 'processo_seletivo']
        db.create_unique(u'vagas_inscricao', ['profissional_id', 'processo_seletivo_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Inscricao', fields ['profissional', 'processo_seletivo']
        db.delete_unique(u'vagas_inscricao', ['profissional_id', 'processo_seletivo_id'])

        # Deleting field 'Inscricao.situacao'
        db.delete_column(u'vagas_inscricao', 'situacao')


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
            'Meta': {'unique_together': "(('profissional', 'processo_seletivo'),)", 'object_name': 'Inscricao'},
            'data': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota_curriculo': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_dinamica': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_escrita': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pretensao_salarial': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'processo_seletivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vagas.ProcessoSeletivo']"}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"}),
            'requisitos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vagas.Requisito']", 'null': 'True', 'blank': 'True'}),
            'situacao': ('django.db.models.fields.IntegerField', [], {})
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