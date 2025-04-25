FROM nginx:1.25-alpine

# Remove default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Create directory for SSL certificates
RUN mkdir -p /etc/nginx/ssl

# Create directory for logs
RUN mkdir -p /var/log/nginx

# Create a non-root user
RUN adduser -D -H -u 1000 -s /bin/bash www-data

# Set proper permissions
RUN chown -R www-data:www-data /var/log/nginx /var/cache/nginx /etc/nginx

# Switch to non-root user
USER www-data

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"] 