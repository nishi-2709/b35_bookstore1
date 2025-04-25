#!/bin/bash

# Configuration
BACKUP_DIR="/backups"
RETENTION_DAYS=7
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.sql.gz"

# Ensure backup directory exists
mkdir -p $BACKUP_DIR

# Perform backup
echo "Starting database backup..."
PGPASSWORD=$POSTGRES_PASSWORD pg_dump -h db -U postgres -d bookstore | gzip > $BACKUP_FILE

# Verify backup
if [ $? -eq 0 ]; then
    echo "Backup completed successfully: $BACKUP_FILE"
    
    # Remove old backups
    find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +$RETENTION_DAYS -delete
    echo "Removed backups older than $RETENTION_DAYS days"
else
    echo "Backup failed!"
    exit 1
fi 