FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package.json ./

# Install dependencies
RUN npm install

# Copy application files
COPY server.js index.html ./

# Expose port
EXPOSE 8080

# Start the application
CMD ["npm", "start"]
