from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import tensorflow
from keras.preprocessing import image
import numpy as np
from brain_tumour import settings


def predict(request):
    if request.method=="POST":
        mfile = request.FILES['image']
        fs = FileSystemStorage()
        fname = fs.save(mfile.name, mfile)
        li1 = ['mri','non_mri']
        path1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "MRIorNOT.hdf5"
        model1 = tensorflow.keras.models.load_model(path1)
        path1 = str(settings.BASE_DIR) + str(settings.STATIC_URL) + fname
        new_img1 = image.load_img(path1, target_size=(224, 224))
        img = image.img_to_array(new_img1)
        img = np.expand_dims(img, axis=0)
        img = img / 255
        pred = model1.predict(img)
        d = pred.flatten()
        j = d.max()
        for index, item in enumerate(d):
            if item == j:
                class_name = li1[index]
                if class_name=="non_mri":
                    message = "Selected file is not an MRI image.."
                    context = {
                        'msg': message,
                    }
                    return render(request, 'predict/Predict_brain_Tumour.html', context)
                else:
                    print(fname)
                    li = ['Brain_Tumour_L1', 'Brain_Tumour_L2', 'Brain_Tumour_L3', 'Brain_Tumour_L4', 'Healthy']
                    path = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "Brain_Tumour.hdf5"
                    model = tensorflow.keras.models.load_model(path)
                    path = str(settings.BASE_DIR) + str(settings.STATIC_URL) + fname
                    new_img = image.load_img(path, target_size=(224, 224))
                    img = image.img_to_array(new_img)
                    img = np.expand_dims(img, axis=0)
                    img = img / 255
                    pred = model.predict(img)
                    d = pred.flatten()
                    j = d.max()
                    for index, item in enumerate(d):
                        if item == j:
                            class_name = li[index]
                            if class_name=="Brain_Tumour_L1":
                                result="Have Level 1 Brain Tumor"
                            elif class_name=="Brain_Tumour_L2":
                                result = "Have Level 2 Brain Tumor"
                            elif class_name == "Brain_Tumour_L3":
                                result = "Have Level 3 Brain Tumor"
                            elif class_name=="Brain_Tumour_L4":
                                result = "Have Level 4 Brain Tumor"
                            elif class_name == "Healthy":
                                result = "Not Have Brain Tumor"
                            c = {
                                "x": result,
                                "img": mfile
                            }
                    return render(request,'predict/Result_Predict.html',c)
    return render(request,'predict/Predict_brain_Tumour.html')


