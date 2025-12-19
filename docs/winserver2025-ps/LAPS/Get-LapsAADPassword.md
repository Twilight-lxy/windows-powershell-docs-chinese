---
description: 在指定的 Microsoft Entra 设备上，查询用于获取 Windows 本地管理员密码解决方案（LAPS）凭据的 Microsoft Entra ID。
external help file: LAPS-help.xml
Module Name: LAPS
online version: https://learn.microsoft.com/powershell/module/laps/get-lapsaadpassword?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
Locale: en-US
ms.date: 04/10/2023
title: Get-LapsAADPassword
---

# 获取LAPS Aad密码

## 摘要
在指定的 Microsoft Entra 设备上，查询用于获取 Windows 本地管理员密码解决方案（LAPS）凭据的 Microsoft Entra ID。

## 语法

```
Get-LapsAADPassword -DeviceIds <String[]> [-IncludePasswords] [-IncludeHistory] [-AsPlainText]
 [<CommonParameters>]
```

## 描述

`Get-LapsAADPassword` cmdlet 允许管理员检索已连接到 Microsoft Entra 的设备的登录密码（LAPS password）及其密码历史记录。该功能是通过使用 `deviceLocalCredentials` 集合向 Microsoft Graph 发送查询来实现的。

`Get-LapsAADPassword` cmdlet 在查询 LAPS 密码时支持两种基本模式：

第一种模式用于查询非敏感的元数据，例如密码备份到 Azure 的时间以及密码的预期过期时间。这种模式要求客户端被授予 Microsoft Graph 的 `DeviceLocalCredential.ReadBasic.All` 权限。

第二种模式会查询所有密码相关信息，包括上述的元数据信息以及密码的明文形式。该模式要求客户端必须具备 Microsoft Graph 的 `DeviceLocalCredential.Read.All` 权限。

`DeviceIds` 参数可以接受设备名称或设备 ID，但底层的 Microsoft Graph 查询仅支持通过设备 ID 进行查询。为了支持这种查询方式，该 cmdlet 会通过发送一个单独的 Microsoft Graph 查询来将输入的设备名称映射到对应的设备 ID。这个额外的查询需要 `Device.Read.All` 权限；如果目标设备是微软管理的桌面设备（Microsoft Managed Desktop），可能还需要 `DeviceManagementManagedDevices.Read.All` 权限。

> [!TIP]
> If there are multiple devices in the tenant with the same name, the cmdlet fails. The workaround
> is to input the device ID directly.

> [!IMPORTANT]
> The `Get-LapsAADPassword` cmdlet is implemented as a wrapper around the Microsoft Graph PowerShell
> library, which must be manually installed on the device before `Get-LapsAADPassword` can work.
> Additional configuration steps are required in your Microsoft Entra tenant to enable authentication to
> Microsoft Graph and to grant the necessary Microsoft Graph permissions. For more information, see
> [开始使用 Windows LAPS 和 Microsoft Entra ID](https://go.microsoft.com/fwlink/?linkid=2233704)

`Verbose` 参数可用于获取有关该 cmdlet 操作的更多信息。

## 示例

### 示例 1

```powershell
Connect-MgGraph -TenantId b20f5886-bddf-43bb-aee6-dda0c87c5fa2 -ClientId 9fa98e34-277f-47fa-9847-e36bdf6bca1f
Get-LapsAADPassword -DeviceIds LAPSAAD
```

```Output
DeviceName DeviceId                             PasswordExpirationTime
---------- --------                             ----------------------
LAPSAAD    dfc6d5f0-225a-4b46-adcf-73a349a31e70 4/22/2023 8:45:29 AM
```

这个示例展示了如何查询由设备名称指定的目标设备的基本LAPS密码元数据信息。

### 示例 2

```powershell
Connect-MgGraph -TenantId b20f5886-bddf-43bb-aee6-dda0c87c5fa2 -ClientId 9fa98e34-277f-47fa-9847-e36bdf6bca1f
Get-LapsAADPassword -DeviceIds dfc6d5f0-225a-4b46-adcf-73a349a31e70 -IncludePasswords
```

```Output
DeviceName             : LAPSAAD
DeviceId               : dfc6d5f0-225a-4b46-adcf-73a349a31e70
Account                : LapsAdmin
Password               : System.Security.SecureString
PasswordExpirationTime : 4/22/2023 8:45:29 AM
PasswordUpdateTime     : 4/11/2023 8:45:29 AM
```

这个示例展示了如何通过设备ID来查询目标设备的完整LAPS密码信息。

### 示例 3

```powershell
Connect-MgGraph -TenantId b20f5886-bddf-43bb-aee6-dda0c87c5fa2 -ClientId 9fa98e34-277f-47fa-9847-e36bdf6bca1f
Get-LapsAADPassword -DeviceIds dfc6d5f0-225a-4b46-adcf-73a349a31e70 -IncludePasswords -AsPlainText
```

```Output
DeviceName             : LAPSAAD
DeviceId               : dfc6d5f0-225a-4b46-adcf-73a349a31e70
Account                : LapsAdmin
Password               : g4q22s[Xz8}!T32[4;Z#0M}v35udF[xB0}iB;P@xk%9E9Tgw,W]7)vx9O!-
PasswordExpirationTime : 4/22/2023 8:45:29 AM
PasswordUpdateTime     : 4/11/2023 8:45:29 AM
```

这个示例展示了如何根据设备ID查询目标设备的完整LAPS密码信息，并以明文形式显示该密码。

### 示例 4

```powershell
Connect-MgGraph -TenantId b20f5886-bddf-43bb-aee6-dda0c87c5fa2 -ClientId 9fa98e34-277f-47fa-9847-e36bdf6bca1f
Get-LapsAADPassword -DeviceIds lapsAAD -IncludePasswords -AsPlainText -IncludeHistory
```

```Output
DeviceName             : LAPSAAD
DeviceId               : dfc6d5f0-225a-4b46-adcf-73a349a31e70
Account                : LapsAdmin
Password               : ]5j)1fi]Rv&Pj+IMiAzq1R9b+yJ.@Q,80#01U541vsC8$Vv${hac8TJlkT8
PasswordExpirationTime : 4/22/2023 8:55:20 AM
PasswordUpdateTime     : 4/11/2023 8:55:21 AM

DeviceName             : LAPSAAD
DeviceId               : dfc6d5f0-225a-4b46-adcf-73a349a31e70
Account                : LapsAdmin
Password               : t&.1P%9891]24I0X4AA4O22a30R1lz(ar7N9{tTf349.Iz{L82O6v{I+,gg
PasswordExpirationTime :
PasswordUpdateTime     : 4/11/2023 8:55:16 AM

DeviceName             : LAPSAAD
DeviceId               : dfc6d5f0-225a-4b46-adcf-73a349a31e70
Account                : LapsAdmin
Password               : g4q22s[Xz8}!T32[4;Z#0M}v35udF[xB0}iB;P@xk%9E9Tgw,W]7)vx9O!-
PasswordExpirationTime :
PasswordUpdateTime     : 4/11/2023 8:45:29 AM
```

这个示例展示了如何查询由设备名称指定的目标设备的完整LAPS密码信息、获取密码历史记录，并以明文形式显示这些密码。

## 参数

### -AsPlainText

请指定此参数，以便以明文格式返回 LAPS 密码。默认情况下，LAPS 密码会封装在一个.NET的**SecureString**对象中返回。

> [!重要提示] > 使用此参数会导致返回的明文密码被随意查看，从而可能带来安全风险。应谨慎使用该参数，仅限于支持或测试场景。

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

### -DeviceIds

指定用于查询 LAPS 凭据的设备名称或设备 ID。

```yaml
Type: System.String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeHistory

指定设备对象上任何较旧的LAPS凭据也应显示出来。

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

### -IncludePasswords

指定是否返回密码信息。

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

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Windows LAPS概述](https://go.microsoft.com/fwlink/?linkid=2233901)

[开始使用 Windows LAPS 和 Microsoft Entra ID](https://go.microsoft.com/fwlink/?linkid=2233704)
