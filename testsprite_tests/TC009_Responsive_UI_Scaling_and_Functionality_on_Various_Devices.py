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
        # -> Resize window or switch to tablet mode to verify UI adjustment without overlap or truncation.
        await page.mouse.wheel(0, await page.evaluate('() => window.innerHeight'))
        

        # -> Resize window or switch to tablet mode to verify UI adjustment without overlap or truncation.
        await page.goto('http://localhost:8080/?device=tablet', timeout=10000)
        await asyncio.sleep(3)
        

        # -> Test all calculator functions on tablet mode to verify functionality.
        frame = context.pages[-1]
        # Input percentage value
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('25')
        

        frame = context.pages[-1]
        # Input number value
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('1000')
        

        frame = context.pages[-1]
        # Click calculate button to test calculation
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Test all calculator functions on tablet mode to ensure full functionality beyond the percentage calculation.
        frame = context.pages[-1]
        # Switch to advanced calculator tab to test other functions
        elem = frame.locator('xpath=html/body/div/div/div/nav/button[2]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Test all calculator functions on tablet mode to ensure full functionality beyond the percentage calculation.
        frame = context.pages[-1]
        # Press '1' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[13]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '+' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[16]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '2' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[14]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '7' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[5]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '⌫' (backspace) button to correct input
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[20]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '3' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[15]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click 'Show History' button to verify history functionality
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div[2]/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Open the app on a mobile device or emulator to verify the UI layout fits the screen and controls respond to touch.
        await page.goto('http://localhost:8080/?device=mobile', timeout=10000)
        await asyncio.sleep(3)
        

        # -> Test all calculator functions on mobile mode to verify full functionality including calculation and history.
        frame = context.pages[-1]
        # Input percentage value on mobile
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('25')
        

        frame = context.pages[-1]
        # Input number value on mobile
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div/div[2]/input').nth(0)
        await page.wait_for_timeout(3000); await elem.fill('1000')
        

        frame = context.pages[-1]
        # Click calculate button on mobile to test calculation
        elem = frame.locator('xpath=html/body/div/div/div/section/form/div[3]/button[3]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Test all calculator functions on mobile mode to verify full functionality including advanced calculations and history.
        frame = context.pages[-1]
        # Switch to advanced calculator tab on mobile to test other functions
        elem = frame.locator('xpath=html/body/div/div/div/nav/button[2]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Test all calculator functions on mobile mode to ensure full functionality beyond the percentage calculation.
        frame = context.pages[-1]
        # Press '1' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[13]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '+' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[16]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '2' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[14]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '7' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[5]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '⌫' (backspace) button to correct input
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[20]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Press '3' button
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div/button[15]').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        frame = context.pages[-1]
        # Click 'Show History' button to verify history functionality
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div[2]/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Verify the history feature works correctly on mobile mode and perform final UI responsiveness review across all device modes.
        frame = context.pages[-1]
        # Click 'Show History' button on mobile to verify history functionality
        elem = frame.locator('xpath=html/body/div/div/div/section[2]/div[2]/button').nth(0)
        await page.wait_for_timeout(3000); await elem.click(timeout=5000)
        

        # -> Perform a final review of UI responsiveness and control accessibility across all device modes to ensure consistent user experience.
        await page.goto('http://localhost:8080/?device=desktop', timeout=10000)
        await asyncio.sleep(3)
        

        await page.goto('http://localhost:8080/?device=tablet', timeout=10000)
        await asyncio.sleep(3)
        

        await page.goto('http://localhost:8080/?device=mobile', timeout=10000)
        await asyncio.sleep(3)
        

        # -> Perform dynamic window resizing tests on desktop and tablet to confirm smooth UI scaling and verify any animations or transitions do not break layout or functionality.
        await page.goto('http://localhost:8080/?device=desktop', timeout=10000)
        await asyncio.sleep(3)
        

        await page.mouse.wheel(0, await page.evaluate('() => window.innerHeight'))
        

        await page.goto('http://localhost:8080/?device=tablet', timeout=10000)
        await asyncio.sleep(3)
        

        await page.mouse.wheel(0, await page.evaluate('() => window.innerHeight'))
        

        # -> Perform final verification of UI responsiveness and control accessibility on mobile mode.
        await page.goto('http://localhost:8080/?device=mobile', timeout=10000)
        await asyncio.sleep(3)
        

        await page.mouse.wheel(0, await page.evaluate('() => window.innerHeight'))
        

        # --> Assertions to verify final state
        frame = context.pages[-1]
        await expect(frame.locator('text=FALCON01 TEAM').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=النسبة المئوية').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=حساب النسب').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=احسب النسب بسهولة ودقة').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=النسبة المئوية (%)').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=استخراج النسبة من العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=إضافة النسبة إلى العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=طرح النسبة من العدد').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=مسح').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=من الآلة').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=احسب').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=آلة حاسبة متقدمة').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=حسابات دقيقة وسريعة').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=C').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=⌫').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=احسب العملية = ').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=إظهار السجل').first).to_be_visible(timeout=30000)
        await expect(frame.locator('text=لا توجد عمليات سابقة').first).to_be_visible(timeout=30000)
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
    