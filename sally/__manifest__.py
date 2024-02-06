# -*- coding: utf-8 -*-
{
    'name': "Flower Shop",

    'summary': """
        Shop for selling flowers """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Farooque Mustafa",
    'website': "https://www.farooquemustafa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'website_sale', 'stock', 'sale_stock'],
    
    'application': True,
    'license': "LGPL-3",
    
    

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/paperformat.xml',
        'data/groups.xml',
        'data/server_action.xml',
        'data/scheduled_action.xml',
        'data/config_parameter.xml',
        'reports/flower_sale_order_views.xml',
        'views/sale_report_action.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/flower_stock_lot_view.xml',
        'views/flower_views.xml',
        'views/product_template_views.xml',
        'views/website_sale_views.xml',
        'views/flower_water_views.xml',
        'views/warehouse_weather_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
