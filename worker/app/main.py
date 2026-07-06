import time


def main():
    print("RAG Worker iniciado correctamente")

    while True:
        print("Worker activo: esperando trabajos de ingesta, Pixie RAG o evaluación...")
        time.sleep(60)


if __name__ == "__main__":
    main()