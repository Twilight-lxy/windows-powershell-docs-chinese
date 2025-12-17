---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 09/19/2017
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsnativeclientapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsNativeClientApplication
---

# 设置 AdfsNativeClient 应用程序

## 摘要
修改 AD FS 中某个应用程序的服务器原生客户端应用程序角色的配置设置。

## 语法

### 标识符（默认值）
```
Set-AdfsNativeClientApplication [-TargetIdentifier] <String> [-Identifier <String>] [-Name <String>]
 [-RedirectUri <String[]>] [-Description <String>] [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 名称
```
Set-AdfsNativeClientApplication [-TargetName] <String> [-Identifier <String>] [-Name <String>]
 [-RedirectUri <String[]>] [-Description <String>] [-LogoutUri <String>] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ApplicationObject
```
Set-AdfsNativeClientApplication [-TargetApplication] <NativeClientApplication> [-Identifier <String>]
 [-Name <String>] [-RedirectUri <String[]>] [-Description <String>] [-LogoutUri <String>] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsNativeClientApplication` 这个 cmdlet 用于修改 Active Directory Federation Services (AD FS) 中某个应用程序的本机客户端应用程序角色的配置设置。

## 示例

## 参数

### -Description
指定一个描述性文字。

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
用于指定一个ID。

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

### -LogoutUri
指定 OAuth 2.0 客户端用于向 AD FS 注册的注销 URI。当 AD FS 启动注销操作时，它会通过在一个 iframe 中显示该 URI 来将客户端的用户代理重定向到这个 URI。此参数的值必须是一个绝对 URI，可以包含查询组件，但不得包含片段组件。只有在安装了 Windows Update KB4038801 之后，才能使用此参数。

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

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

客户端指定的重定向URI必须已经在中间件（AD FS）中注册。该URI必须与该OAuth 2.0客户端的标识符相匹配。如果客户端ID和重定向URI对应于一个已预先注册的OAuth 2.0客户端，并且资源所有者通过提供自己的凭据授权了访问权限，那么中间件（AD FS）会通过将客户端用户的用户代理重定向到这个重定向URI来传递授权代码或访问令牌。

此参数的值必须与 OAuth 2.0 客户端在请求授权时指定的重定向 URI 完全匹配。这包括路径末尾的斜杠（/），如果需要的话。我们建议在重定向 URI 中使用更安全的协议，例如 HTTPS。

对于那些通过使用 Windows Web Authentication Broker 进行身份验证的 Windows 应用程序，应使用 `ms-app://` 协议作为重定向 URI。如果您正在开发一个 Windows 应用程序，可以使用以下代码片段来获取该应用程序的重定向 URI：

```csharp
Uri redirectURI = Windows.Security Authentication.Web.WebAuthenticationBroker.GetCurrentApplicationCallbackUri();
```

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetApplication
指定本机客户端应用程序。

```yaml
Type: NativeClientApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定原生客户端应用程序的ID。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定原生客户端应用程序的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

字符串对象通过 *Description*（描述）、*Identifier*（标识符）、*Name*（名称）、*RedirectUri*（重定向URI）、*TargetIdentifier*（目标标识符）和 *TargetName*（目标名称）这些参数被接收。

### Microsoft IdentityServer.Management.Resources NativeClientApplication

`NativeClientApplication` 对象是通过 `TargetApplication` 参数接收到的。

## 输出

### Microsoft IdentityServer.Management.Resources NativeClientApplication

当指定 *PassThru* 参数时，该命令会返回更新后的 NativeClientApplication 对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-AdfsNativeClientApplication](./Add-AdfsNativeClientApplication.md)

[Get-AdfsNativeClientApplication](./Get-AdfsNativeClientApplication.md)

[Remove-AdfsNativeClientApplication](./Remove-AdfsNativeClientApplication.md)

