---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Configuration.dll-Help.xml
Module Name: ADRMS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrms/install-adrms?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-ADRMS
---

# 安装 ADRMS

## 摘要
配置一个新的 AD RMS 服务器部署。

## 语法

### MainProvisioningParameterSet
```
Install-ADRMS [-Path] <String> [-Credential <PSCredential>] [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ADFSProvisioningParameterSet
```
Install-ADRMS [-ADFSUrl] <String> [-Credential <PSCredential>] [-Force] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Install-ADRMS` cmdlet 用于配置 Active Directory Rights Management Services (AD RMS) 服务器角色。在运行此 cmdlet 之前，首先需要创建一个 Windows PowerShell 驱动器，指定 ADRmsInstall 提供程序以及安装类型（RootCluster、LicensingCluster 或 JoinCluster）作为该驱动器的根目录。接着，需要为驱动器中的容器和子项设置属性，以指定配置服务器所需的初始值。

## 示例

### 示例 1：配置 AD RMS
```
PS C:\> Install-ADRMS -Path adrmsDrive:\
```

此命令通过使用先前在 `adrmsdrive:\` 目录中的项目上设置的配置参数来配置 AD RMS。有关如何使用此 cmdlet 的更多信息，请参阅 [使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)。

### 示例 2：配置身份联合（Identity Federation）支持并设置联合服务器URL
```
PS C:\> Install-ADRMS -ADFSUrl https://sampleadfsurl.com -Force
```

此命令为 AD RMS 集群配置了身份联合支持功能，并设置了联合服务器的 URL。

## 参数

### -ADFSUrl
配置 AD RMS 集群以支持 Active Directory Federation Services (AD FS)，并指定联合服务器的 URL。

```yaml
Type: String
Parameter Sets: ADFSProvisioningParameterSet
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
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

### -Credential
指定用于配置过程的用户凭据。如果指定了此参数，系统会提示您输入凭据。该参数的用法与“RunAs”命令类似。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
通过覆盖那些可能阻止命令成功执行的限制来强制完成该命令（只要所做的更改不会危及安全性）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定提供者驱动器及其路径，或者是当前驱动器上的相对路径。此参数是必需的。可以使用点（.）来表示当前位置。该参数不支持通配符，且没有默认值。

```yaml
Type: String
Parameter Sets: MainProvisioningParameterSet
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### PSCredential

### 字符串（string）

## 输出

## 备注

## 相关链接

