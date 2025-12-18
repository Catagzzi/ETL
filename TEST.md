# IMPORTANT IMPLEMENTATION REQUIREMENT

Your implementation must be written in Python and use one of the following data-processing frameworks:

Apache Beam (Python SDK)
Apache Spark using the Python API (PySpark)

Coding Challenge - Build a Real-Time ETL Pipeline with CDC

At Aladia, we’re building scalable systems that power real-world applications - from live analytics to distributed learning platforms. We believe great engineers don't just ship code - they reason through ambiguity, make informed trade-offs, and design with purpose.

This challenge is designed to assess your architectural thinking, coding ability, and communication clarity.

## 🎯 Goal

Design and implement a functional end-to-end ETL pipeline that ingests and transforms change data in real time. Your pipeline should reflect the kind of infrastructure we use at Aladia: fast-moving, modular, and robust.

## 🧩 Your Mission

Construct a pipeline that includes the following components:

## 📂 Source Database

Choose any SQL or NoSQL database and model sample data (e.g., orders, devices, user activity). The database should simulate ongoing writes and updates.

## 🧬 Change Data Capture (CDC)

Implement CDC to detect and extract changes (inserts, updates, deletes) as they happen. You may use tools like Debezium, MongoDB Change Streams, or implement a custom polling solution.

## 🔍 Justify your choice:

What makes your CDC approach suitable? What trade-offs are involved in latency, consistency, or operational complexity?

## 📨 Message Queue

Push CDC events into a message queue such as Kafka, RabbitMQ, or Redis Streams to decouple producers and consumers.

🔍 How do you handle delivery semantics? What strategies are used for retries, ordering, or deduplication?

⚙️ Data Processing with Apache Spark

Consume from the queue and process the data using Apache Spark. Transform, clean, and enrich the events so they are analytics-ready.

Bonus: Can your Spark jobs handle malformed input or schema evolution gracefully?

## 🏛️ Data Warehouse Sink

Load the final transformed data into a warehousing solution like BigQuery, Redshift, or Snowflake. Design the schema to support downstream querying.

🔍 Explain how you’d scale this if the volume grows 10x. What would break first?

## 📦 Deliverables

A GitHub repo containing:

- Source code for each pipeline component.

- A README.md that includes:

- Setup instructions (preferably with Docker Compose).

- An architecture diagram.

- A rationale for each design choice and component.

- Discussion of trade-offs, edge cases, and limitations.

## Bonus:

A simple demo script or Jupyter notebook that runs sample queries on the final warehouse.

Tests or logging that show how each component is working (or failing safely).

# ✅ Evaluation Criteria

We’re looking for a balance between working code and engineering reasoning. Specifically:

## 👷 Modularity: Is each part of the pipeline well-isolated and maintainable?

## 🧠 Clarity of thought: Do you explain why you made certain choices, not just what you did?

## 🚨 Resilience: Does your pipeline fail gracefully?

## 🚀 Extensibility: Would this architecture scale with data volume or team size?
