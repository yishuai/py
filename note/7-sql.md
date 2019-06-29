# declarative languages

In declarative languages such as SQL & Prolog:
A "program" is a description of the desired result
The interpreter figures out how to generate the result

In imperative languages such as Python & Scheme:
A "program" is a description of computational processes
The interpreter carries out execution/evaluation rules

# Structured Query Language (SQL)

The SQL language is an ANSI and ISO standard, but DBMS's implement custom variants

A select statement creates a new table, either from scratch or by projecting a table

A create table statement gives a global name to a table

Lots of other statements exist: analyze, delete, explain, insert, replace, update, etc.

Most of the important action is in the select statement

Install sqlite (version 3.8.3 or later): http://sqlite.org/download.html
Use sqlite online: https://sql.cs61a.org

# Select Statements Project Existing Tables

order by [order]
