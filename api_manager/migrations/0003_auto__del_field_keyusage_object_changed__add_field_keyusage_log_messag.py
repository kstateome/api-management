# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Deleting field 'KeyUsage.object_changed'
        db.delete_column('api_manager_keyusage', 'object_changed')

        # Adding field 'KeyUsage.log_message'
        db.add_column('api_manager_keyusage', 'log_message', self.gf('django.db.models.fields.CharField')(default='', max_length=250), keep_default=False)

        # Changing field 'KeyUsage.date'
        db.alter_column('api_manager_keyusage', 'date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True))
    
    
    def backwards(self, orm):
        
        # Adding field 'KeyUsage.object_changed'
        db.add_column('api_manager_keyusage', 'object_changed', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Deleting field 'KeyUsage.log_message'
        db.delete_column('api_manager_keyusage', 'log_message')

        # Changing field 'KeyUsage.date'
        db.alter_column('api_manager_keyusage', 'date', self.gf('django.db.models.fields.DateField')())
    
    
    models = {
        'api_manager.keys': {
            'Meta': {'object_name': 'Keys'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'key_user': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'api_manager.keyusage': {
            'Meta': {'object_name': 'KeyUsage'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api_management.Keys']"}),
            'log_message': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }
    
    complete_apps = ['api_manager']
