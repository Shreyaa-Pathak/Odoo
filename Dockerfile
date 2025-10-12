FROM odoo:17.0
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
COPY ./config/odoo.conf /etc/odoo/odoo.conf
COPY ./server /mnt/odoo
RUN chown -R odoo:odoo /mnt/odoo /etc/odoo
EXPOSE 8069
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
