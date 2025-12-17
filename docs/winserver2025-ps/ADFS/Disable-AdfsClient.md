---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfsclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsClient
---

# 禁用 AdfsClient

## 摘要
禁用当前已在 AD FS 中注册的 OAuth 2.0 客户端。

## 语法

### 名称（默认值）
```
Disable-AdfsClient [[-TargetName] <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ClientId
```
Disable-AdfsClient [-TargetClientId] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Disable-AdfsClient [-TargetClient] <AdfsClient> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-AdfsClient` cmdlet 用于禁用当前已在 Active Directory Federation Services (AD FS) 中注册的 OAuth 2.0 客户端。禁用该客户端后，AD FS 将不再授权来自该 OAuth 2.0 客户端的资源访问请求。

## 示例

### 示例 1：禁用一个 OAuth 2.0 客户端
```
PS C:\> Disable-AdfsClient -TargetName "Payroll Application"
```

此命令将禁用当前在 AD FS 中注册的 OAuth 2.0 客户端。

## 参数

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

### -TargetClient
指定要禁用的已注册的 OAuth 2.0 客户端。

```yaml
Type: AdfsClient
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClientId
指定要禁用的已注册 OAuth 2.0 客户端的标识符。

```yaml
Type: String
Parameter Sets: ClientId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定要禁用的已注册的 OAuth 2.0 客户端的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: False
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftIdentityServer.Management.Resources.AdfsClient

`AdfsClient` 对象是通过 `*TargetClient` 参数接收到的。

### System.String

字符串对象是通过*TargetClientId*和*TargetName*参数接收到的。

## 输出

### MicrosoftIdentityServer.Management.Resources.AdfsClient

当指定*PassThru*参数时，该命令会返回一个处于禁用状态的AdfsClient对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-AdfsClient](./Add-AdfsClient.md)

[Enable-AdfsClient](./Enable-AdfsClient.md)

[Get-AdfsClient](./Get-AdfsClient.md)

[Remove-AdfsClient](./Remove-AdfsClient.md)

[Set-AdfsClient](./Set-AdfsClient.md)

