import grpc
import vector_pb2
import vector_pb2_grpc
import event_pb2

def run():
    # Connect to the vector-aggregator gRPC server
    channel = grpc.insecure_channel('localhost:50051')
    stub = vector_pb2_grpc.VectorStub(channel)
    
    fields = {
        "field1": event_pb2.Value(integer=123),
        "message": event_pb2.Value(boolean=True),
    }

    log = event_pb2.Log(
        fields=fields,
        value=event_pb2.Value(
            map=event_pb2.ValueMap(
                fields={
                    "field1": event_pb2.Value(integer=123),
                    "message": event_pb2.Value(raw_bytes=b"Hello World"),
                }
            )    
        ),
    )
    
    event_wrapper = event_pb2.EventWrapper(log=log)

    # Create a PushEventsRequest
    push_events_request = vector_pb2.PushEventsRequest(events=[event_wrapper])

    # Send the request to the server
    response = stub.PushEvents(push_events_request)

    # Print the response
    print(response)

if __name__ == '__main__':
    run()
