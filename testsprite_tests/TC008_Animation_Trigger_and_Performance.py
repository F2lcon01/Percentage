import asyncio
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None
    
    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()
        
        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",         # Set the browser window size
                "--disable-dev-shm-usage",        # Avoid using /dev/shm which can cause issues in containers
                "--ipc=host",                     # Use host-level IPC for better stability
                "--single-process"                # Run the browser in a single process mode
            ],
        )
        
        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        context.set_default_timeout(5000)
        
        # Open a new page in the browser context
        page = await context.new_page()
        
        # Navigate to your target URL and wait until the network request is committed
        await page.goto("http://localhost:8080", wait_until="commit", timeout=10000)
        
        # Wait for the main page to reach DOMContentLoaded state (optional for stability)
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=3000)
        except async_api.Error:
            pass
        
        # Iterate through all iframes and wait for them to load as well
        for frame in page.frames:
            try:
                await frame.wait_for_load_state("domcontentloaded", timeout=3000)
            except async_api.Error:
                pass
        
        # Interact with the page elements to simulate user flow
        # -> Click the 'احسب' (Calculate) button to trigger animations and observe UI response.
        frame = context.pages[-1]
        # Click the 'احسب' (Calculate) button to trigger animations and observe UI response.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Fill the required input field (index 3) with a valid number and perform calculation again to observe animation.
        frame = context.pages[-1]
        # Fill the 'النسبة المئوية (%)' input field with 25 to enable calculation.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('25')
        

        frame = context.pages[-1]
        # Fill the 'العدد' input field with 1000 to enable calculation.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('1000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform rapid input changes in the percentage and number fields to observe UI animation performance and check for any lag, flicker, or glitches.
        frame = context.pages[-1]
        # Change percentage input to 10 rapidly to test animation performance.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('10')
        

        frame = context.pages[-1]
        # Change number input to 500 rapidly to test animation performance.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('500')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations during rapid input changes.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform a series of rapid consecutive calculations with varying inputs to further stress test animation smoothness and UI responsiveness.
        frame = context.pages[-1]
        # Change percentage input to 15 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('15')
        

        frame = context.pages[-1]
        # Change number input to 2000 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('2000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Continue performing rapid consecutive calculations with varying inputs to further stress test animation smoothness and UI responsiveness.
        frame = context.pages[-1]
        # Change percentage input to 5 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('5')
        

        frame = context.pages[-1]
        # Change number input to 1500 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('1500')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Continue performing rapid consecutive calculations with varying inputs to further stress test animation smoothness and UI responsiveness.
        frame = context.pages[-1]
        # Change percentage input to 20 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('20')
        

        frame = context.pages[-1]
        # Change number input to 3000 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('3000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Continue performing rapid consecutive calculations with varying inputs to further stress test animation smoothness and UI responsiveness.
        frame = context.pages[-1]
        # Change percentage input to 30 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('30')
        

        frame = context.pages[-1]
        # Change number input to 4000 for rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('4000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform additional rapid consecutive calculations with different input values to further confirm animation smoothness under stress.
        frame = context.pages[-1]
        # Change percentage input to 40 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('40')
        

        frame = context.pages[-1]
        # Change number input to 5000 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('5000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Continue performing rapid consecutive calculations with varying inputs to further stress test animation smoothness and UI responsiveness.
        frame = context.pages[-1]
        # Change percentage input to 50 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('50')
        

        frame = context.pages[-1]
        # Change number input to 6000 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('6000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Continue performing rapid consecutive calculations with varying inputs to further stress test animation smoothness and UI responsiveness.
        frame = context.pages[-1]
        # Change percentage input to 60 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('60')
        

        frame = context.pages[-1]
        # Change number input to 7000 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('7000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Continue performing rapid consecutive calculations with varying inputs to further stress test animation smoothness and UI responsiveness.
        frame = context.pages[-1]
        # Change percentage input to 70 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('70')
        

        frame = context.pages[-1]
        # Change number input to 8000 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('8000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform a few more rapid consecutive calculations with different input values to confirm animation smoothness under stress and then test animations on other interactive elements or tabs.
        frame = context.pages[-1]
        # Change percentage input to 80 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('80')
        

        frame = context.pages[-1]
        # Change number input to 9000 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('9000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform a few more rapid consecutive calculations with different input values to confirm animation smoothness under stress and then test animations on other interactive elements or tabs.
        frame = context.pages[-1]
        # Change percentage input to 90 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('90')
        

        frame = context.pages[-1]
        # Change number input to 10000 for further rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('10000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform the final rapid consecutive calculation with different input values to confirm animation smoothness under stress and conclude testing.
        frame = context.pages[-1]
        # Change percentage input to 100 for final rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('100')
        

        frame = context.pages[-1]
        # Change number input to 11000 for final rapid consecutive calculation test.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('11000')
        

        frame = context.pages[-1]
        # Click the 'احسب' button to trigger calculation and observe animations.
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        await expect(frame.locator('text=FALCON01 TEAM').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=النسبة المئوية').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=حاسبة النسبة المئوية - احسب النسب بسهولة ودقة').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=النسبة المئوية (%)').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=طريقة الحساب:').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text= - استخراج النسبة من العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text= - إضافة النسبة إلى العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text= - طرح النسبة من العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=مسح').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=من الآلة').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=احسب').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=100% من 11000 = ١١٬٠٠٠').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=© 2026 Falcon01 Team. All Rights Reserved.').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=Official Certified Site').first).to_be_visible(timeout=30000)
        await asyncio.sleep(5)
    
    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()
            
asyncio.run(run_test())
    