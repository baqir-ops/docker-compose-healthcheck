FROM alpine:3.19

HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
    CMD pgrep sh || exit 1

CMD ["sh", "-c", "echo 'Logger sidecar started' && while true; do echo \"[$(date '+%Y-%m-%d %H:%M:%S')] Logger running...\"; sleep 10; done"]
