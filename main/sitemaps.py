from django.contrib import sitemaps 
from django.urls import reverse
      
       
class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq ="daily"

    def items(self):
        return [
            'main:home',
            'main:about',
            'main:contact',
        ]
    def location(self, item):
        return reverse(item)
        