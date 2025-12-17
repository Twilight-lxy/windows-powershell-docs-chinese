---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/enable-adfsclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-AdfsClient
---

# 启用 AdfsClient

## 摘要
启用通过 AD FS 进行 OAuth 2.0 客户端注册的功能。

## 语法

### 名称（默认值）
```
Enable-AdfsClient [[-TargetName] <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ClientId
```
Enable-AdfsClient [-TargetClientId] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Enable-AdfsClient [-TargetClient] <AdfsClient> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Enable-AdfsClient` cmdlet 允许使用 Active Directory Federation Services (AD FS) 的 OAuth 2.0 客户端注册功能。使用此 cmdlet 可以启用当前处于禁用状态的已注册 OAuth 2.0 客户端。如果 AD FS 收到来自已注册但未启用的 OAuth 2.0 客户端的授权请求，它会拒绝该客户端访问相应的资源。

## 示例

### 示例 1：启用一个 OAuth 2.0 客户端
```
PS C:\> Enable-AdfsClient -TargetName "Payroll Application"
```

此命令启用由名称“Payroll Application”标识的已注册的 OAuth 2.0 客户端。

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
指定要启用的已注册的 OAuth 2.0 客户端。

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
用于指定已注册的 OAuth 2.0 客户端的标识符，以便启用该客户端的功能。

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
指定要启用的已注册的 OAuth 2.0 客户端的名称。

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
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft_identityServer.Management Resources.AdfsClient

`AdfsClient` 对象是通过 `*TargetClient*` 参数接收到的。

### System.String

字符串对象是通过*TargetClientId*和*TargetName*参数接收到的。

## 输出

### Microsoft_identityServer.Management Resources.AdfsClient

当指定*PassThru*参数时，会返回已启用的AdfsClient对象。默认情况下，此cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-AdfsClient](./Add-AdfsClient.md)

[Disable-AdfsClient](./Disable-AdfsClient.md)

[Get-AdfsClient](./Get-AdfsClient.md)

[Remove-AdfsClient](./Remove-AdfsClient.md)

[Set-AdfsClient](./Set-AdfsClient.md)

