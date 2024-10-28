from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time
from PuzzleSolver import PuzzleSolver

class PuzzleServer(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        received_array = json.loads(post_data)
        print(f'Received array: {received_array}')
        initial = int(''.join(map(str, received_array)))
        solver = PuzzleSolver(initial)
        path = self.path.strip('/')

        start_time = time.time()

        if path == 'bfs':
            solvable, m, nodes_expanded = solver.solve_bfs()
        elif path == 'dfs':
            solvable, m, nodes_expanded, maxdepth = solver.solve_dfs()
        elif path == 'ids':
            solvable, m, nodes_expanded = solver.solve_ids()
        elif path == 'astar_manhattan':
            solvable, m, nodes_expanded = solver.solve_astar(0)
        elif path == 'astar_euclidean':
            solvable, m, nodes_expanded = solver.solve_astar(1)
        else:
            self.send_response(404)
            self.end_headers()
            return

        end_time = time.time()
        total_time = end_time - start_time
        response_array = solver.get_directions(solver.get_path(m)) if solvable else []
        print(f'Response array: {response_array}')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = {
            'array': response_array,
            'nodes_expanded': nodes_expanded,
            'solvable': solvable,
            'totaltime': f"{int(total_time * 1000)} ms",
            'cost': len(response_array),
            'maxdepth': maxdepth if path == 'dfs' else len(response_array)
        }
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=PuzzleServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()