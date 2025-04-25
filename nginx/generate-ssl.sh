#!/bin/bash

# Create SSL directory if it doesn't exist
mkdir -p ssl

# Generate private key
openssl genrsa -out ssl/key.pem 2048

# Generate CSR
openssl req -new -key ssl/key.pem -out ssl/csr.pem -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"

# Generate self-signed certificate
openssl x509 -req -days 365 -in ssl/csr.pem -signkey ssl/key.pem -out ssl/cert.pem

# Set proper permissions
chmod 600 ssl/key.pem
chmod 644 ssl/cert.pem

echo "SSL certificates generated successfully!"
echo "Certificate: ssl/cert.pem"
echo "Private key: ssl/key.pem" 