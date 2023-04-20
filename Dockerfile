FROM golang:1.18-buster as builder

WORKDIR /app

COPY go.* ./
RUN go mod download

COPY invoke.go ./

RUN go build -mod=readonly -v -o server

# Use the official dbt-bigquery image for running
# https://github.com/dbt-labs/dbt-bigquery/pkgs/container/dbt-bigquery

FROM ghcr.io/dbt-labs/dbt-bigquery:1.4.1

WORKDIR /

COPY --from=builder /app/server /app/server
COPY script.sh ./

ENTRYPOINT ["/app/server"]