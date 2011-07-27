# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Keys.active'
        db.add_column('api_manager_keys', 'active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Keys.active'
        db.delete_column('api_manager_keys', 'active')
    
    
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
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['api_management.Keys']"}),
            'object_changed': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['api_manager']
