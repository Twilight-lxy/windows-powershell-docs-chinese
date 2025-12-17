---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/disable-adfsendpoint?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AdfsEndpoint
---

# 禁用 AdfsEndpoint

## 摘要
禁用 AD FS 的一个端点。

## 语法

### 地址
```
Disable-AdfsEndpoint [[-TargetAddressPath] <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TargetObject
```
Disable-AdfsEndpoint [-TargetEndpoint] <Endpoint> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### FullUrl
```
Disable-AdfsEndpoint [-TargetFullUrl] <Uri> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Disable-AdfsEndpoint` 这个 cmdlet 用于禁用 Active Directory Federation Services (AD FS) 的某个终端点。

## 示例

#### 示例 1：禁用一个端点
```
PS C:\> Disable-AdfsEndpoint -TargetAddressPath "/adfs/services/trust/13/Windows"
```

此命令会禁用当前联合服务器上的 WS-Trust 1.3 终端。

## 参数

### -PassThru
返回一个对象，该对象表示您正在操作的项。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetAddressPath
指定端点的地址路径。该 cmdlet 会禁用您指定的端点。例如，这样的路径可以是 `/adfs/portal/updatepassword`。

```yaml
Type: String
Parameter Sets: Address
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetEndpoint
指定要禁用的端点。该值通常来自管道（pipeline）。

```yaml
Type: Endpoint
Parameter Sets: TargetObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetFullUrl
指定要禁用的端点的完整URL。

```yaml
Type: Uri
Parameter Sets: FullUrl
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### MicrosoftIdentityServer.PowerShell.Resources Endpoint
一个用于表示联邦服务（Federation Service）端点的类。

## 输出

### 无

## 备注
* Endpoints provide access to the federation server functionality of AD FS, such as token issuance and the publishing of federation metadata. Depending on the type of endpoint, you can enable or disable the endpoint or control whether the endpoint is published to Web Application Proxy.

## 相关链接

[Enable-AdfsEndpoint](./Enable-AdfsEndpoint.md)

[Get-AdfsEndpoint](./Get-AdfsEndpoint.md)

[Set-AdfsEndpoint](./Set-AdfsEndpoint.md)

