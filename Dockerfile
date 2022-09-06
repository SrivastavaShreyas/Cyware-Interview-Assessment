# CYWARE INTERVIEW ASSESSMENT

# Using Ubuntu latest image as the base image
FROM ubuntu

# Installing Nginx
RUN apt-get -y update && apt-get -y install nginx

# Copy static web page code to the nginx module
COPY index.html /var/www/html/

# Expose the access port 
EXPOSE 80/tcp

# Run the nginx server
CMD [ "nginx", "-g", "daemon off;"]

