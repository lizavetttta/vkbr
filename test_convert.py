from aspose.threed import Scene

# Загрузка модели
scene = Scene.from_file("test_model.obj")

# Сохранение в другой формат
scene.save("test_model.stl")

print("Конвертация выполнена: test_model.stl")