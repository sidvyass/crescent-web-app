from django.shortcuts import render
from django.templatetags.static import static
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    images = [
        ("dock_install.jpg", "Dock Install", "/services/dock-install-storage/"),
        ("dock_storage.jpg", "Dock Storage", "/services/dock-install-storage/"),
        ("outdoor_power_washing.jpg", "Exterior Power Washing", "/services/powerwashing/"),
        ("landscaping.jpg", "Landscaping", "/services/landscaping/"),
        ("painting.jpg", "Painting", "/services/painting/"),
        ("side_walk_powerwashing.jpg", "Sidewalk Powerwashing", "/services/powerwashing/"),
        ("snow_removal.jpg", "Snow Removal", "/services/snow-removal/"),
        ("tree_removal.jpg", "Tree Removal", "/services/tree-removal/"),
    ]

    if request.method == "POST":
        first = request.POST.get("firstName")
        last = request.POST.get("lastName")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        zip_code = request.POST.get("zipcode")
        service_type = request.POST.get("serviceType")
        notes = request.POST.get("notes")

        message = f"""
        New Contact Form Submission:

        Name: {first} {last}
        Email: {email}
        Phone: {phone}
        Zip Code: {zip_code}
        Service Type: {service_type}
        Notes: {notes}
        """

        send_mail(
            subject="New Contact Form Submission",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["jack@crescentservices.co", "dev@crescentservices.co"],
        )

        return render(request, 'core/success.html')

    service_slides = [images[i:i+4] for i in range(0, len(images), 4)]

    return render(request, 'core/home.html', {
        "service_slides": service_slides,
    })


def contact_us(request):
    if request.method == "POST":
        first = request.POST.get("firstName")
        last = request.POST.get("lastName")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        zip_code = request.POST.get("zipcode")
        service_type = request.POST.get("serviceType")
        notes = request.POST.get("notes")

        message = f"""
        New Contact Form Submission:

        Name: {first} {last}
        Email: {email}
        Phone: {phone}
        Zip Code: {zip_code}
        Service Type: {service_type}
        Notes: {notes}
        """

        send_mail(
            subject="New Contact Form Submission",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["jack@crescentservices.co", "siddharth.vyas619@gmail.com"],
        )

        return render(request, 'core/success.html')
    return render(request, 'core/contact_us.html')


def terms_and_conditions(request):
    return render(request, 'core/t_and_c.html')


def about_us(request):
    return render(request, 'core/about_us.html')


SERVICE_CONTEXT = {
    'landscaping': {
        'hero_image_url': static('core/images/services/landscaping/hero.jpg'),
        'hero_heading': 'Our Landscaping Services',
        'intro_text': 'From initial design to ongoing care, we turn your outdoor space into something beautiful.',
        'services': [
            {
                'title': 'Lawn Care',
                'image_url': static('core/images/services/landscaping/image1.jpg'),
                'description': 'Our lawn care services include mowing, edging, fertilizing, and weed control tailored to your yard’s unique needs. We use only premium equipment and materials to ensure consistent results. Whether it’s weekly maintenance or seasonal treatments, our experienced team delivers lush, healthy lawns that stand out. Trust us to bring out the full potential of your green space.'
            },
            {
                'title': 'Garden Design',
                'image_url': static('core/images/services/landscaping/image2.jpg'),
                'description': 'We don’t just plant flowers—we craft experiences. Our garden designs blend functionality, seasonal color, and native plants to create vibrant outdoor spaces. With an eye for detail and a deep understanding of horticulture, we design gardens that thrive long-term. Every project is customized to reflect your lifestyle and preferences.'
            },
            {
                'title': 'Hardscaping',
                'image_url': static('core/images/services/landscaping/image3.jpg'),
                'description': "From stunning stone patios to practical retaining walls, our hardscaping services enhance both usability and curb appeal. We focus on craftsmanship, durability, and cohesive design integration with your landscape. Whether you're entertaining guests or creating a quiet outdoor retreat, our installations are built to last and elevate your property."
            },
            {
                'title': 'Leaf Removal',
                'image_url': static('core/images/services/landscaping/image4.jpg'),
                'description': 'Fall leaves and debris can suffocate your lawn and create a mess. Our professional cleanup services ensure your property remains neat, healthy, and prepared for every season. We go beyond just raking—our team thoroughly clears beds, trims back dead growth, and disposes of everything responsibly. You get a fresh start without lifting a finger.'
            },
        ]
    },
    'dock-install-storage': {
        'hero_image_url': static('core/images/services/dock-install-storage/hero.jpg'),
        'hero_heading': 'Let’s Talk Dock!',
        'intro_text': 'Whether you need a new dock or seasonal storage, we handle it from start to finish.',
        'services': [
            {
                'title': 'Installation',
                'image_url': static('core/images/services/dock-install-storage/image2.jpg'),
                'description': 'Our dock installation service ensures a stable, secure, and visually appealing waterfront setup tailored to your property. We use high-quality materials, follow local regulations, and prioritize safety and longevity in every build. With years of experience, we deliver seamless, worry-free installations that you can rely on season after season.'
            },
            {
                'title': 'Storage',
                'image_url': static('core/images/services/dock-install-storage/image3.jpg'),
                'description': 'Proper off-season storage is critical to extending the life of your dock. We carefully disassemble, transport, and securely store your dock components to shield them from harsh weather and damage. Our team handles every detail, so you can enjoy peace of mind knowing your dock is protected and ready for reinstallation when needed.'
            },
            {
                'title': 'Maintenance',
                'image_url': static('core/images/services/dock-install-storage/image1.jpg'),
                'description': 'Regular dock maintenance ensures safe use and prevents costly damage. We inspect for structural wear, tighten hardware, and address any issues before they become major problems. Our proactive approach keeps your dock looking great and functioning at its best—so it’s always ready when you are.'
            },
            {
                'title': 'Seasonal Cleanup',
                'image_url': static('core/images/services/dock-install-storage/image4.jpg'),
                'description': 'Seasonal transitions can take a toll on your dock area. We offer full-service cleanups to clear away debris, algae, and sediment build-up around your dock. Whether prepping for summer or wrapping up the season, we leave your waterfront pristine, safe, and welcoming for all your activities.'
            },
        ]
    },
    'powerwashing': {
        'hero_image_url': static('core/images/services/powerwashing/hero.jpg'),
        'hero_heading': 'For All Things Powerwashing!',
        'intro_text': 'Restore the look of your property with our professional powerwashing services. We clean deep, protect your surfaces, and leave everything looking brand new.',
        'services': [
            {
                'title': 'Exterior House Refresh',
                'image_url': static('core/images/services/powerwashing/image2.jpg'),
                'description': 'Bring back the shine to your home’s exterior with our low-pressure house washing service. We gently remove built-up dirt, mildew, and algae from siding, trim, and gutters without causing damage. Our environmentally safe techniques protect your paint and landscaping while giving your home a crisp, clean finish that lasts.'
            },
            {
                'title': 'Sidewalk & Driveway Revival',
                'image_url': static('core/images/services/powerwashing/image3.jpg'),
                'description': 'Your walkways and driveways take a beating from foot traffic, weather, and grime. We cut through stains, moss, and oil buildup to restore the clean, even look of your concrete or pavers. With our commercial-grade powerwashers and trained team, we make your entryway safer, cleaner, and more inviting.'
            },
            {
                'title': 'Walls, Fences & Stone Cleaning',
                'image_url': static('core/images/services/powerwashing/image1.jpg'),
                'description': 'Brick, vinyl, stucco, or stone—we clean it all. Our wall washing service lifts away years of dirt, mold, and discoloration to bring out your surface’s natural color and texture. It’s an instant facelift for your property that enhances both beauty and value.'
            },
            {
                'title': 'Dock & Deck Powerwash',
                'image_url': static('core/images/services/powerwashing/image4.jpg'),
                'description': 'Waterfront areas are magnets for algae and grime. Our dock and deck cleaning service is tailored to these sensitive spaces. We remove buildup that can make surfaces slippery or unsightly, using methods that preserve the integrity of your wood or composite materials. Start the season with a dock that looks as good as the view.'
            },
        ]
    },
    'painting': {
        'hero_image_url': static('core/images/services/painting/hero.jpg'),
        'hero_heading': 'Professional Painting Services',
        'intro_text': 'Breathe new life into your home or business with crisp, clean, and lasting finishes—inside and out.',
        'services': [
            {
                'title': 'Exterior Painting',
                'image_url': static('core/images/services/painting/image2.jpg'),
                'description': 'Your exterior paint is your property’s first impression—and we make sure it’s a great one. We use weather-resistant, premium-grade paint to protect your surfaces from the elements while adding curb appeal. Every job includes surface prep, sanding, and priming to ensure long-lasting results that won’t peel, crack, or fade prematurely.'
            },
            {
                'title': 'Interior Painting',
                'image_url': static('core/images/services/painting/image3.jpg'),
                'description': 'From single rooms to entire homes, we deliver clean, smooth finishes with minimal disruption. We protect your floors and furniture, handle all prep work, and leave behind nothing but flawless color. Whether you’re going for bold and modern or warm and classic, we help you bring your vision to life with precision.'
            },
            {
                'title': 'Trim & Detail Work',
                'image_url': static('core/images/services/painting/image1.jpg'),
                'description': 'Crisp lines and clean edges make all the difference in professional paintwork. Our trim, molding, and detail painting services add elegance and polish to any room. We take our time with the small stuff—because it’s the small stuff that sets your space apart.'
            },
            {
                'title': 'Deck & Fence Staining',
                'image_url': static('core/images/services/painting/image4.jpg'),
                'description': 'Keep your deck and fence protected and looking fresh with our expert staining and sealing services. We remove old finishes, sand down surfaces, and apply high-quality stains that enhance the wood grain and block moisture. It’s both beauty and durability—all in one coat.'
            },
        ]
    },
    'snow-removal': {
        'hero_image_url': static('core/images/services/snow-removal/hero.jpg'),
        'hero_heading': 'Reliable Snow & Ice Removal',
        'intro_text': 'Stay safe and stress-free all winter long with our fast, dependable snow and ice removal services.',
        'services': [
            {
                'title': 'Driveway & Sidewalk Clearing',
                'image_url': static('core/images/services/snow-removal/image2.jpg'),
                'description': 'We keep your driveways, sidewalks, and entry paths clear and safe during winter storms. Using plows, blowers, and hand tools, our team removes snow efficiently without damaging surfaces. We prioritize prompt service to help you avoid slips, fines, or delays getting where you need to go.'
            },
            {
                'title': 'Salting & Ice Control',
                'image_url': static('core/images/services/snow-removal/image3.jpg'),
                'description': 'Ice can be invisible—but the risk is real. We apply salt and de-icing agents strategically to prevent black ice from forming and reduce slippery surfaces. Our treatments are fast-acting, long-lasting, and safe for pets and plants when needed. Safety and accessibility are always our top priorities.'
            },
            {
                'title': 'Commercial Lot Plowing',
                'image_url': static('core/images/services/snow-removal/image1.jpg'),
                'description': 'Businesses can’t afford downtime. Our commercial snow plowing ensures your lots, loading zones, and customer entrances stay open and accessible no matter the forecast. We work on-call or on schedule, with equipment sized for large surfaces and quick turnarounds—even during back-to-back storms.'
            },
            {
                'title': 'Roof Snow Removal',
                'image_url': static('core/images/services/snow-removal/image4.jpg'),
                'description': 'Heavy roof snow can lead to ice dams, leaks, or structural stress. Our team uses specialized tools and safety protocols to clear snow from your roof without causing damage. Prevent long-term issues and give your home the protection it needs when winter piles up.'
            },
        ]
    },
    'tree-removal': {
        'hero_image_url': static('core/images/services/tree-removal/hero.jpg'),
        'hero_heading': 'Safe & Professional Tree Removal',
        'intro_text': 'Whether it’s for safety, aesthetics, or space—our expert team removes trees with precision and care.',
        'services': [
            {
                'title': 'Full Tree Removal',
                'image_url': static('core/images/services/tree-removal/image2.jpg'),
                'description': 'We safely remove dead, hazardous, or unwanted trees of all sizes from your property. Using advanced equipment and experienced crews, we make sure the job is done without damaging surrounding structures or landscaping. Every cut is controlled, every cleanup is thorough, and your safety is our priority.'
            },
            {
                'title': 'Stump Grinding',
                'image_url': static('core/images/services/tree-removal/image3.jpg'),
                'description': 'Leftover stumps are more than an eyesore—they attract pests and hinder landscaping. Our stump grinding service removes them efficiently below ground level, allowing you to repurpose the area or reseed seamlessly. Fast, clean, and complete—no more tripping hazards or lawn equipment obstacles.'
            },
            {
                'title': 'Emergency Tree Removal',
                'image_url': static('core/images/services/tree-removal/image1.jpg'),
                'description': 'Storm damage? Fallen limbs? We respond quickly to emergencies, removing fallen or dangerous trees before they cause more harm. Our team is available after severe weather or accidents to secure your property and restore safety fast. Trust us for fast, reliable, and insured emergency response.'
            },
            {
                'title': 'Lot Clearing & Brush Removal',
                'image_url': static('core/images/services/tree-removal/image4.jpg'),
                'description': 'Planning construction or just reclaiming space? We offer full lot clearing and brush removal for residential and commercial properties. Our process is efficient and thorough, removing small trees, undergrowth, and debris to give you a clean slate. We prep your land right the first time.'
            },
        ]
    },
}

def services_view(request, service_type):
    if request.method == "POST":
        first = request.POST.get("firstName")
        last = request.POST.get("lastName")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        zip_code = request.POST.get("zipcode")
        service_type = request.POST.get("serviceType")
        notes = request.POST.get("notes")

        message = f"""
        New Contact Form Submission:

        Name: {first} {last}
        Email: {email}
        Phone: {phone}
        Zip Code: {zip_code}
        Service Type: {service_type}
        Notes: {notes}
        """

        send_mail(
            subject="New Contact Form Submission",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["jack@crescentservices.co"],
        )

        return render(request, 'core/success.html')

    context = SERVICE_CONTEXT.get(service_type)
    if not context:
        raise Http404()
    return render(request, 'core/services.html', context)

