from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SNS, SQS
from diagrams.aws.storage import S3, Storage
from diagrams.digitalocean.network import Certificate, LoadBalancer
from diagrams.gcp.database import SQL
from diagrams.generic.compute import Rack
from diagrams.generic.os import LinuxGeneral
from diagrams.generic.place import Datacenter
from diagrams.onprem.database import Mongodb, MySQL, PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Caddy, Nginx, Traefik
from diagrams.onprem.queue import Celery, Kafka, RabbitMQ
from diagrams.programming.framework import (Angular, Backbone, Django, Ember,
                                            FastAPI, Flask, Flutter, GraphQL,
                                            Laravel, Micronaut, Rails, React,
                                            Spring, Starlette, Vue)
from diagrams.programming.language import (PHP, Bash, C, Cpp, Csharp, Dart,
                                           Elixir, Erlang, Go, Java,
                                           Javascript, Kotlin, Latex, Matlab,
                                           NodeJS, Python, R, Ruby, Rust,
                                           Scala, Swift, Typescript)

DEFAULT_ICON_CLASS = Rack


class DockerImagePattern:
    pattern = r""
    diagram_render_class = None

    def render(self, service_name):
        return self.diagram_render_class(service_name)


class RedisImage(DockerImagePattern):
    pattern = r"redis:"
    diagram_render_class = Redis


class PostgreSQLImage(DockerImagePattern):
    pattern = r"postgres:"
    diagram_render_class = PostgreSQL


class NginxImage(DockerImagePattern):
    pattern = r"nginx"
    diagram_render_class = Nginx


class PythonImage(DockerImagePattern):
    pattern = r"^python"
    diagram_render_class = Python


class MysqlImage(DockerImagePattern):
    pattern = r"^mysql"
    diagram_render_class = MySQL


class SNSImage(DockerImagePattern):
    pattern = r"^sns$"
    diagram_render_class = SNS


class SQSImage(DockerImagePattern):
    pattern = r"^sqs"
    diagram_render_class = SQS


class DynamoDBImage(DockerImagePattern):
    pattern = r"^dynamodb"
    diagram_render_class = Dynamodb


class RubbyImage(DockerImagePattern):
    pattern = r"^ruby"
    diagram_render_class = Ruby


class GolangImage(DockerImagePattern):
    pattern = r"^golang"
    diagram_render_class = Go


class RabbitMQImage(DockerImagePattern):
    pattern = r"^rabbitmq"
    diagram_render_class = RabbitMQ


class DjangoImage(DockerImagePattern):
    pattern = r"^django$"
    diagram_render_class = Django


class CeleryImage(DockerImagePattern):
    pattern = r"^celery$"
    diagram_render_class = Celery


class FlaskImage(DockerImagePattern):
    pattern = r"^flask$"
    diagram_render_class = Flask


class S3Image(DockerImagePattern):
    pattern = r"^s3$"
    diagram_render_class = S3


class RailsImage(DockerImagePattern):
    pattern = r"^rails"
    diagram_render_class = Rails


class RustImage(DockerImagePattern):
    pattern = r"^rust"
    diagram_render_class = Rust


class KotlinImage(DockerImagePattern):
    pattern = r"^kotlin"
    diagram_render_class = Kotlin


class NodeJSImage(DockerImagePattern):
    pattern = r"^node"
    diagram_render_class = NodeJS


class JavaScriptImage(DockerImagePattern):
    pattern = r"^javascript"
    diagram_render_class = Javascript


class MongodbImage(DockerImagePattern):
    pattern = r"^mongo"
    diagram_render_class = Mongodb


class ReactImage(DockerImagePattern):
    pattern = r"^react"
    diagram_render_class = React


class VueImage(DockerImagePattern):
    pattern = r"^vue"
    diagram_render_class = Vue


class KafkaImage(DockerImagePattern):
    pattern = r"^kafka"
    diagram_render_class = Kafka


class TraefikImage(DockerImagePattern):
    pattern = r"^traefik"
    diagram_render_class = Traefik


class CaddyImage(DockerImagePattern):
    pattern = r"^caddy"
    diagram_render_class = Caddy


class FastAPIImage(DockerImagePattern):
    pattern = r"^fastapi"
    diagram_render_class = FastAPI


class AngularImage(DockerImagePattern):
    pattern = r"^angular"
    diagram_render_class = Angular


class BackboneImage(DockerImagePattern):
    pattern = r"^backbone"
    diagram_render_class = Backbone


class EmberImage(DockerImagePattern):
    pattern = r"^ember"
    diagram_render_class = Ember


class FlutterImage(DockerImagePattern):
    pattern = "^flutter"
    diagram_render_class = Flutter


class GraphqlImage(DockerImagePattern):
    pattern = r"^graphql$"
    diagram_render_class = GraphQL


class LaravelImage(DockerImagePattern):
    pattern = r"^laravel$"
    diagram_render_class = Laravel


class MicronautImage(DockerImagePattern):
    pattern = r"^micronaut$"
    diagram_render_class = Micronaut


class SpringImage(DockerImagePattern):
    pattern = r"^spring"
    diagram_render_class = Spring


class StarletteImage(DockerImagePattern):
    pattern = r"^starlette$"
    diagram_render_class = Starlette


class BashImage(DockerImagePattern):
    pattern = r"^bash$"
    diagram_render_class = Bash


class CImage(DockerImagePattern):
    pattern = r"^c$"
    diagram_render_class = C


class CPPImage(DockerImagePattern):
    pattern = r"^cpp$"
    diagram_render_class = Cpp


class CSharpImage(DockerImagePattern):
    pattern = r"^csharp$"
    diagram_render_class = Csharp


class DartImage(DockerImagePattern):
    pattern = r"^dart"
    diagram_render_class = Dart


class ElixirImage(DockerImagePattern):
    pattern = r"^elixir"
    diagram_render_class = Elixir


class ErlangImage(DockerImagePattern):
    pattern = r"^erlang"
    diagram_render_class = Erlang


class JavaImage(DockerImagePattern):
    pattern = r"^java"
    diagram_render_class = Java


class LatexImage(DockerImagePattern):
    pattern = r"^latex"
    diagram_render_class = Latex


class MatlabImage(DockerImagePattern):
    pattern = r"^matlab$"
    diagram_render_class = Matlab


class PHPImage(DockerImagePattern):
    pattern = r"^php"
    diagram_render_class = PHP


class RImage(DockerImagePattern):
    pattern = r"^R$"
    diagram_render_class = R


class ScalaImage(DockerImagePattern):
    pattern = r"^scala"
    diagram_render_class = Scala


class SwiftImage(DockerImagePattern):
    pattern = r"^swift"
    diagram_render_class = Swift


class TypeScriptImage(DockerImagePattern):
    pattern = r"^typescript"
    diagram_render_class = Typescript


class DatacenterImage(DockerImagePattern):
    pattern = r"^datacenter$"
    diagram_render_class = Datacenter


class StorageImage(DockerImagePattern):
    pattern = r"^storage$"
    diagram_render_class = Storage


class LinuxGeneralImage(DockerImagePattern):
    pattern = r"^linuxgeneral$"
    diagram_render_class = LinuxGeneral


class SQLImage(DockerImagePattern):
    pattern = r"^sql$"
    diagram_render_class = SQL


class RackImage(DockerImagePattern):
    pattern = r"^rack$"
    diagram_render_class = Rack


class CertificateImage(DockerImagePattern):
    pattern = r"^certificate$"
    diagram_render_class = Certificate


class LoadBalancerImage(DockerImagePattern):
    pattern = r"^loadbalancer$"
    diagram_render_class = LoadBalancer
