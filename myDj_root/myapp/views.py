from django.shortcuts import render, redirect
from myapp.models import Content, Device
from django.db.models import F

#home page
def index(request):
    #for device deletion from table
    if request.method=="POST" and 'devicedeletion' in request.POST:
        Device.objects.filter(devicename=request.POST.get('devicedeletion')).delete()
        return redirect('myapp:home')
    #for content deletion from table
    elif request.method=="POST" and 'contentdeletion' in request.POST:
        Content.objects.filter(filename=request.POST.get('contentdeletion')).delete()
        return redirect('myapp:home')
 
    allContent = Content.objects.all()
    allDevices = Device.objects.all()
    return render(request, 'home.html', {'allDevices': allDevices, 'allContent': allContent})


def uploads(request):
     #pick device for showing playlist
    if request.method=="POST" and 'showPlaylist' in request.POST:
        currentDevice = Device.objects.get(devicename=request.POST.get('dn'))
        showDevice = currentDevice.imagePlaylist.all()
        for img in showDevice:
            print(img.filename)

        allContent = Content.objects.all()
        allDevices = Device.objects.all()
        return render(request, 'upload.html', {'allDevices': allDevices, 'allContent': allContent, 'showDevice': showDevice, 'currentDevice':currentDevice})

    #delete image from playlist
    elif request.method=="POST" and 'imageRemove' in request.POST:
        currentDevice = Device.objects.get(devicename=(request.POST.get('curDevice')))
        currentImage = Content.objects.get(filename=(request.POST.get('imageName')))
        currentDevice.imagePlaylist.remove(currentImage)
        Content.objects.filter(filename=(request.POST.get('imageName'))).update(active=F('active') - 1)
        allContent = Content.objects.all()
        allDevices = Device.objects.all()
        showDevice = currentDevice.imagePlaylist.all()
        return render(request, 'upload.html', {'allDevices': allDevices, 'allContent': allContent, 'showDevice': showDevice, 'currentDevice':currentDevice})

    #close shown playlist
    elif request.method=="POST" and 'closePlaylist' in request.POST:
        allContent = Content.objects.all()
        allDevices = Device.objects.all()
        return render(request, 'upload.html', {'allDevices': allDevices, 'allContent': allContent, 'showDevice': ""})

    #if image is uploaded this post request goes 
    elif request.method=="POST" and 'imageUpload' in request.POST:
        image = request.FILES['image']
        count = 1
        imageName = ""
        if request.POST.get('imageName') == "":
            imageName = image.name
        else:
            imageName = request.POST.get('imageName')
        temp = imageName
        if(' ' not in temp):
            #basicaly the while loops makes it so if you upload an image with the same name it just puts a (1) after it
            print("image made")
            while(Content.objects.filter(filename=temp).count()):
                temp = imageName + "(" + str(count) + ")"
                count += 1
            Content.objects.create(filename=temp, file=image)
        return redirect('myapp:uploads')

    #if a new device is made this post goes
    elif request.method=="POST" and 'deviceCreation' in request.POST:
        n = request.POST.get('deviceName')
        d = request.POST.get('description')
        l = request.POST.get('location')
        print(n + " " + d + " " + l)
        if Device.objects.filter(devicename=n).count() == 0:
            Device.objects.create(devicename=n, description=d, location=l)
            print("created")
        return redirect('myapp:uploads')

    #images added to playlist
    elif request.method=="POST" and 'playlist' in request.POST:
        deviceForPlaylist = request.POST.get('deviceName')
        playlistImages = request.POST.getlist('playlistImages')
        device = Device.objects.get(devicename=deviceForPlaylist)
        for img in playlistImages:
            temp = Content.objects.filter(filename=img)
            temp.update(active=F('active') + 1)
            device.imagePlaylist.add(Content.objects.get(filename=img))

        for img in device.imagePlaylist.all():
            print(img.filename)
        return redirect('myapp:uploads')

    allContent = Content.objects.all()
    allDevices = Device.objects.all()
    return render(request, 'upload.html', {'allDevices': allDevices, 'allContent': allContent, 'showDevice': ""})

def playlist(request):

    return render(request, 'playlist.html')