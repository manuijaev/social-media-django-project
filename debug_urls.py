import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media.settings')
django.setup()

from django.urls import get_resolver

def list_all_urls():
    """List all available URLs in the project"""
    resolver = get_resolver()
    
    print("Available URLs:")
    print("-" * 50)
    
    def print_patterns(patterns, prefix=''):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                # This is an include
                print(f"INCLUDE: {prefix}{pattern.pattern} -> {getattr(pattern, 'app_name', 'No app name')}")
                print_patterns(pattern.url_patterns, prefix + str(pattern.pattern))
            else:
                # This is a direct pattern
                print(f"URL: {prefix}{pattern.pattern} -> {pattern.name or 'No name'}")
    
    print_patterns(resolver.url_patterns)

if __name__ == "__main__":
    list_all_urls()