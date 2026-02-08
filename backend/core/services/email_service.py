"""
Email Service for Authentication

This module provides email sending functionality for authentication flows,
including email verification and password reset.
"""

import os
import logging
from typing import Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class EmailService:
    """
    Email service for sending authentication-related emails

    In development, emails are logged to console.
    In production, configure SMTP settings via environment variables.
    """

    def __init__(self):
        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_port = int(os.getenv("SMTP_PORT", "587"))
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.from_email = os.getenv("FROM_EMAIL", "noreply@todoapp.com")
        self.app_url = os.getenv("APP_URL", "http://localhost:3000")

        # Determine if we're in production mode
        self.is_production = all([
            self.smtp_host,
            self.smtp_user,
            self.smtp_password
        ])

        if not self.is_production:
            logger.info("Email service running in development mode (console logging)")

    def send_verification_email(self, to_email: str, verification_token: str) -> bool:
        """
        Send email verification email to user

        Args:
            to_email: Recipient email address
            verification_token: Verification token for email confirmation

        Returns:
            True if email sent successfully, False otherwise
        """
        subject = "Verify your email address"
        verification_url = f"{self.app_url}/verify-email?token={verification_token}"

        body = f"""
Hello,

Thank you for registering with our Todo application!

Please verify your email address by clicking the link below:

{verification_url}

This link will expire in 24 hours.

If you did not create an account, please ignore this email.

Best regards,
Todo App Team
        """

        return self._send_email(to_email, subject, body)

    def send_password_reset_email(self, to_email: str, reset_token: str) -> bool:
        """
        Send password reset email to user

        Args:
            to_email: Recipient email address
            reset_token: Password reset token

        Returns:
            True if email sent successfully, False otherwise
        """
        subject = "Reset your password"
        reset_url = f"{self.app_url}/reset-password?token={reset_token}"

        body = f"""
Hello,

We received a request to reset your password for your Todo application account.

Click the link below to reset your password:

{reset_url}

This link will expire in 1 hour.

If you did not request a password reset, please ignore this email and your password will remain unchanged.

Best regards,
Todo App Team
        """

        return self._send_email(to_email, subject, body)

    def _send_email(self, to_email: str, subject: str, body: str) -> bool:
        """
        Internal method to send email

        In development mode, logs email to console.
        In production mode, sends via SMTP.

        Args:
            to_email: Recipient email address
            subject: Email subject
            body: Email body

        Returns:
            True if email sent successfully, False otherwise
        """
        if not self.is_production:
            # Development mode - log to console
            logger.info(f"""
================================================================================
EMAIL SENT (Development Mode)
================================================================================
To: {to_email}
From: {self.from_email}
Subject: {subject}
Time: {datetime.utcnow().isoformat()}

{body}
================================================================================
            """)
            return True

        # Production mode - send via SMTP
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            message = MIMEMultipart()
            message["From"] = self.from_email
            message["To"] = to_email
            message["Subject"] = subject

            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(message)

            logger.info(f"Email sent successfully to {to_email}")
            return True

        except Exception as e:
            logger.error(f"Failed to send email to {to_email}: {str(e)}")
            return False


# Singleton instance
email_service = EmailService()
