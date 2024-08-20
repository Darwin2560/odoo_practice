python3 odoo-bin -r user -w password --addons-path=addons -d odoo
python3 odoo-bin -r user -w password --addons-path=addons -d odoo -i base
python3 odoo-bin scaffold school modules

python3 odoo-bin -r user -w password --addons-path=addons,modules -d odoo
python3 odoo-bin -r user -w password --addons-path=addons,modules -d odoo -u school
