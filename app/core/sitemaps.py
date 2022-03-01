from django.contrib.sitemaps import Sitemap
from main.models import Help, NeedHelp
from django.urls import reverse

# class HelpSitemap(Sitemap):
#     changefreq = 'always'
#     priority = 0.8
#     protocol = 'https'

#     def items(self):
#         return Help.objects.all()

#     def lastmod(self, obj):
#         return obj.mod_date

#     def location(self):
#         return 'help_list/'

# class NeedHelpSitemap(Sitemap):
#     changefreq = 'always'
#     priority = 0.8
#     protocol = 'https'

#     def items(self):
#         return NeedHelp.objects.all()

#     def lastmod(self, obj):
#         return obj.mod_date

#     def location(self):
#         return 'need_help_list/'

class StaticSitemap(Sitemap):
    changefreq = "always"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['map','help', 'need_help',
         'index', 'need_help', 'help_list',
         'need_help_list']

    def location(self, item):
        return reverse(item)