# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import snort_pb2 as snort__pb2


class ControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddRules = channel.unary_unary(
        '/snort.Controller/AddRules',
        request_serializer=snort__pb2.AddRule.SerializeToString,
        response_deserializer=snort__pb2.SnortReply.FromString,
        )
    self.StartSnort = channel.unary_unary(
        '/snort.Controller/StartSnort',
        request_serializer=snort__pb2.ControlSnort.SerializeToString,
        response_deserializer=snort__pb2.SnortReply.FromString,
        )
    self.StopSnort = channel.unary_unary(
        '/snort.Controller/StopSnort',
        request_serializer=snort__pb2.ControlSnort.SerializeToString,
        response_deserializer=snort__pb2.SnortReply.FromString,
        )


class ControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddRules(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartSnort(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopSnort(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddRules': grpc.unary_unary_rpc_method_handler(
          servicer.AddRules,
          request_deserializer=snort__pb2.AddRule.FromString,
          response_serializer=snort__pb2.SnortReply.SerializeToString,
      ),
      'StartSnort': grpc.unary_unary_rpc_method_handler(
          servicer.StartSnort,
          request_deserializer=snort__pb2.ControlSnort.FromString,
          response_serializer=snort__pb2.SnortReply.SerializeToString,
      ),
      'StopSnort': grpc.unary_unary_rpc_method_handler(
          servicer.StopSnort,
          request_deserializer=snort__pb2.ControlSnort.FromString,
          response_serializer=snort__pb2.SnortReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'snort.Controller', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
