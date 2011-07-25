# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Keys'
        db.create_table('api_management_keys', (
            ('key_user', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('api_management', ['Keys'])

        # Adding model 'KeyUsage'
        db.create_table('api_management_keyusage', (
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('object_changed', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api_management.Keys'])),
        ))
        db.send_create_signal('api_management', ['KeyUsage'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Keys'
        db.delete_table('api_management_keys')

        # Deleting model 'KeyUsage'
        db.delete_table('api_management_keyusage')
    
    
    models = {
        'api_management.keys': {
            'Meta': {'object_name': 'Keys'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'key_user': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'api_management.keyusage': {
            'Meta': {'object_name': 'KeyUsage'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api_management.Keys']"}),
            'object_changed': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['api_management']
