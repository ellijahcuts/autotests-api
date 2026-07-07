from concurrent import futures

import grpc

import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        print(f"Получен запрос к курсу {request.course_id} от пользователя {request.username}")
        return course_service_pb2.GetCourseResponse(message=f"Доступ к курсу предоставлен для пользователя {request.username}",course_id=f"{request.course_id}", title="Автотесты API", description="Будем изучать написание API автотестов")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('GRPC server is running... port 50051...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()