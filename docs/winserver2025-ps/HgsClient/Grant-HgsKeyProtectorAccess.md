---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/grant-hgskeyprotectoraccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Grant-HgsKeyProtectorAccess
---

# 授予 HGSKeyProtector 访问权限

## 摘要
为关键保护者授予访问守护者的权限。

## 语法

### InputObject

```
Grant-HgsKeyProtectorAccess -KeyProtector <CimInstance> -Guardian <CimInstance>
 [-AllowUntrustedRoot] [-AllowExpired] [<CommonParameters>]
```

### FriendlyName
```
Grant-HgsKeyProtectorAccess -KeyProtector <CimInstance> -GuardianFriendlyName <String>
 [-AllowUntrustedRoot] [-AllowExpired] [<CommonParameters>]
```

## 描述

`Grant-HgsKeyProtectorAccess` cmdlet 授予主机守护服务（Host Guardian Service）的守护者对密钥保护器（key protector）的访问权限。此操作需要密钥保护器所有者的私有签名密钥。

## 示例

### 示例 1：授予监护人访问权限

```powershell
$Owner        = Get-HgsGuardian -Name "Guardian06"
$Guardian01   = Get-HgsGuardian -Name "Guardian11"
$KeyProtector = New-HgsKeyProtector -Owner $Owner
Grant-HgsKeyProtectorAccess -KeyProtector $KeyProtector -Guardian $Guardian01
```

第一个命令使用 `Get-HgsGuardian` cmdlet 获取名为 `Guardian06` 的守护对象，然后将该对象存储在 `$Owner` 变量中。

第二个命令获取名为 `Guardian11` 的 Guardian 对象，然后将其存储在 `$Guardian01` 变量中。

第三个命令用于创建一个密钥保护器。该命令将存储在 `$Owner` 中的 `Guardian06` 定义为“所有者”（**Owner**）。

最后的命令为密钥保护者提供了对存储在 `$Guardian01` 中的守护程序（guardian）的访问权限。

## 参数

### -AllowExpired

表示此cmdlet可以为监护人授予权限，而该监护人持有的证书已经过期。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowUntrustedRoot

表示此cmdlet可以为使用自签名证书的守护程序授予权限。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Guardian

指定一个监护人，允许其访问该密钥。

```yaml
Type: CimInstance
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -GuardianFriendlyName

为守护者指定一个友好的名称。

```yaml
Type: String
Parameter Sets: FriendlyName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KeyProtector

指定要授予访问权限的关键保护器。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### CimInstance#MSFT_HgsKeyProtector

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径指定了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[New-HgsKeyProtector](./New-HgsKeyProtector.md)

[Revoke-HgsKeyProtectorAccess](./Revoke-HgsKeyProtectorAccess.md)

[Get-HgsGuardian](./Get-HgsGuardian.md)
