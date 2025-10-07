# Security Measures

- CSRF protection enabled via `{% csrf_token %}` in all forms.
- SQL injection prevented using Django ORM and validated forms.
- XSS mitigated with browser headers and CSP.
- Cookies secured with HTTPS-only flags.

# HTTPS and Security Configuration

## Django Settings
- `SECURE_SSL_REDIRECT = True`: Redirects all HTTP traffic to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enforces HTTPS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to subdomains.
- `SECURE_HSTS_PRELOAD = True`: Enables browser preload of HSTS.
- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are sent over HTTPS.
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF tokens are sent over HTTPS.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser XSS protection.

## Deployment
- SSL configured via Nginx with Let's Encrypt certificates.
- HTTP traffic redirected to HTTPS.

## Review
- All settings verified in production.
- Manual tests confirm secure redirects and headers.

