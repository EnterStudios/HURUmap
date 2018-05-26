from django.core.management.base import BaseCommand, CommandError

import wbdata
from hurumap.models.data import DataIndicatorAuthor, DataIndicator, DataIndicatorValue


class Command(BaseCommand):
    help = 'Scrape WorldBank Data Indicators'

    def handle(self, *args, **options):
        author, created = DataIndicatorAuthor.objects.get_or_create(
            slug='world-bank',
            defaults={
                'name': 'World Bank',
                'url': 'https://worldbank.org/',
                'description': 'Hello'
            }
        )

        wb_indicators = wbdata.get_indicator()
        for wb_indicator in wb_indicators:
            if wb_indicator.get('id', 'lema') == 'lema':
                raise CommandError(str(wb_indicator))
            
            indicator, created = DataIndicator.objects.get_or_create(
                author=author,
                author_code=wb_indicator.get('id'),
                defaults={
                    'author_data': wb_indicator,
                    'name': wb_indicator.get('name'),
                    'source': wb_indicator.get('source'),
                    'source_note': wb_indicator.get('sourceNote'),
                    'topics': list(wb_indicator.get('topics'))
                }
            )

            # takwimu_countries = 
            wb_indicator_values = wbdata.get_data(
                wb_indicator.get('id'),
                country=[
                    "KE", "NG", "SN", "TZ", "BF",
                    "ZM", "ZA", "UG", "ET", "CD"
                ]
            )
            for wb_indicator_val in wb_indicator_values:
                indicator_val, created = DataIndicatorValue.objects.get_or_create(
                    indicator=indicator,
                    country=wb_indicator_val.get('country'),
                    date=wb_indicator_val.get('date'),
                    defaults={
                        'author_data': wb_indicator_val,
                        'decimal': wb_indicator_val.get('decimal'),
                        'value': wb_indicator_val.get('value')
                    }
                )
                self.stdout.write(self.style.SUCCESS('Successfully created indicator value"%s"' % wb_indicator.get('id')))

            self.stdout.write(self.style.SUCCESS('Successfully created indicator "%s"' % wb_indicator.get('id')))
            