FROM python:3.11-slim AS build

# Copy the application code and configuration
ADD . /

# Set environment variables
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=.

EXPOSE 5035 5036 5037 5038 5039

# Install Python packages
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the remaining files
COPY . .

# Set the container command
CMD [ "python3", "./tb_modbus_drilling_rig_emulator/drilling_rig_modbus_emulator.py" ]