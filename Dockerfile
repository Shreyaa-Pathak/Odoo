# Base Odoo 18 image
FROM odoo:18.0

# Locale setup
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=Asia/Kathmandu

# Copy Odoo config file
COPY ./config/odoo.conf /etc/odoo/odoo.conf

# Copy custom addons (if you have them)
# Keep this folder *light* — only core or required ones
COPY ./server /mnt/odoo

# Adjust ownership
USER root
RUN mkdir -p /mnt/extra-addons /var/lib/odoo && \
    chown -R odoo:odoo /mnt/odoo /mnt/extra-addons /var/lib/odoo /etc/odoo

USER odoo

# Default ports
EXPOSE 8069 8071

# Entry command
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
