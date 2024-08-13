# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable for the database URL
ENV DATABASE_URL=postgresql://hotel_booking_3tcn_user:bN6IEnlGykQcdQkdNn30Xiazm0U1WpFa@dpg-cqkei0rqf0us73c8nb2g-a.oregon-postgres.render.com/hotel_booking_3tcn

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]



