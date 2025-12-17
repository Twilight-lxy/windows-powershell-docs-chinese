---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 09/19/2017
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsnativeclientapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsNativeClientApplication
---

# 添加 AdfsNativeClient 应用程序

## 摘要
在 Active Directory Federation Services (AD FS) 中为某个应用程序添加一个本机客户端应用程序角色。

## 语法

### ApplicationGroupIdentifier（默认值）
```
Add-AdfsNativeClientApplication [-ApplicationGroupIdentifier] <String> [-Name] <String> [-Identifier] <String>
 [[-RedirectUri] <String[]>] [-Description <String>] [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ApplicationGroupObject
```
Add-AdfsNativeClientApplication [-ApplicationGroup] <ApplicationGroup> [-Name] <String> [-Identifier] <String>
 [[-RedirectUri] <String[]>] [-Description <String>] [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-AdfsNativeClientApplication` cmdlet 用于在 Active Directory Federation Services (AD FS) 中为某个应用程序添加一个“原生客户端应用程序”角色。

## 示例

## 参数

### -ApplicationGroup
指定一个应用程序组。

```yaml
Type: ApplicationGroup
Parameter Sets: ApplicationGroupObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroupIdentifier
指定一个应用程序组的ID。

```yaml
Type: String
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Description
指定一个描述信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Identifier
指定一个标识符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -LogoutUri
指定 OAuth 2.0 客户端用于向 AD FS 注册的登出（logout）URI。当 AD FS 启动登出流程时，它会通过在一个 iframe 中显示该 URI 来将客户端用户的用户代理（user-agent）重定向到此 URI。此参数的值必须是一个绝对 URI，可以包含查询参数（query component），但不允许包含片段参数（fragment component）。只有在安装了 Windows Update KB4038801 后，此参数才可用。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您当前正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RedirectUri
用于指定一组重定向URI，供OAuth 2.0客户端注册到AD FS（Active Directory Federation Services）中。当OAuth 2.0客户端请求访问AD FS中的资源时，需要提供这些重定向URI以完成授权过程。

客户端指定的重定向URI必须已经注册在AD FS中，并且该URI必须与该OAuth 2.0客户端的标识符相对应。如果客户端ID和重定向URI对应于一个预先注册的OAuth 2.0客户端，并且资源所有者通过提供自己的凭据授权访问，那么AD FS会通过将客户端用户的用户代理（user-agent）重定向到这个重定向URI来提供授权代码或访问令牌。

这个参数的值必须与OAuth 2.0客户端在请求授权时指定的重定向URI完全匹配。这包括末尾的斜杠（/），如果需要的话。我们建议在重定向URI中使用更安全的协议，例如https。

对于那些使用 Windows Web Authentication Broker 进行身份验证的 Windows 应用程序，应使用 `ms-app://` 方案作为重定向 URI。如果您正在开发一个 Windows 应用程序，请通过以下代码片段来获取该应用程序的重定向 URI：

`Uri redirectURI = Windows.Security Authentication.Web.WebAuthenticationBrokerGetCurrentApplicationCallbackUri();`

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftIdentityServer.Management.Resources.ApplicationGroup

`ApplicationGroup` 对象是通过 `ApplicationGroup` 参数接收到的。

### System.String

`String` 对象通过 `ApplicationGroupIdentifier`、`Description`、`Identifier`、`Name` 和 `RedirectUri` 参数被接收。

## 输出

### MicrosoftIdentityServerManagement.Resources.NativeClientApplication

当指定*PassThru*参数时，会返回一个新的NativeClientApplication对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Get-AdfsNativeClientApplication](./Get-AdfsNativeClientApplication.md)

[Remove-AdfsNativeClientApplication](./Remove-AdfsNativeClientApplication.md)

[Set-AdfsNativeClientApplication](./Set-AdfsNativeClientApplication.md)

