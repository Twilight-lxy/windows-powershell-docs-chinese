---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapterAdvancedProperty.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapteradvancedproperty?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapterAdvancedProperty
---

# Get-NetAdapterAdvancedProperty

## 摘要
获取网络适配器的高级属性。

## 语法

### 按名称排序（默认设置）
```
Get-NetAdapterAdvancedProperty [[-Name] <String[]>] [-IncludeHidden] [-AllProperties]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByNameRegistryKeyword
```
Get-NetAdapterAdvancedProperty [[-Name] <String[]>] -RegistryKeyword <String[]> [-IncludeHidden]
 [-AllProperties] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByNameDisplayName
```
Get-NetAdapterAdvancedProperty [[-Name] <String[]>] -DisplayName <String[]> [-IncludeHidden] [-AllProperties]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByInstanceIDKeyword
```
Get-NetAdapterAdvancedProperty -InterfaceDescription <String[]> -RegistryKeyword <String[]> [-IncludeHidden]
 [-AllProperties] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByInstanceIDDisplayName
```
Get-NetAdapterAdvancedProperty -InterfaceDescription <String[]> -DisplayName <String[]> [-IncludeHidden]
 [-AllProperties] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```
Get-NetAdapterAdvancedProperty -InterfaceDescription <String[]> [-IncludeHidden] [-AllProperties]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapterAdvancedProperty` cmdlet 可用于获取网络适配器的高级属性。默认情况下，该 cmdlet 会返回那些具有显示名称（display name）的高级属性，这些属性会在 Windows 用户界面中的“适配器属性”（Adapter Properties）的“高级”（Advanced）选项卡中显示出来。对于没有显示名称的高级属性，则需要指定 `AllProperties` 参数才能将其获取到。此外，也可以通过 `DisplayName` 或 `RegistryKeyword` 参数来选择特定的高级属性。这两个参数都支持使用通配符字符。

这些高级属性通常存储在注册表中的以下位置：  
`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\xxxxxxxx`  
其中，`xxxx` 是一个四位字符的字符串，表示一个整数（例如 0007）。标准化的关键词其注册表关键字名称以星号 “*” 开头。可以通过将输出结果传递给 `Format-List` cmdlet，并指定 `ValidDisplayValues` 或 `ValidRegistryValues` 参数，来查看这些关键词的有效值。

## 示例

### 示例 1：根据指定的显示名称，获取所有可见网络适配器的所有高级属性
```
PS C:\> Get-NetAdapterAdvancedProperty -Name "*"
```

这个命令会获取所有可见网络适配器中具有显示名称的所有高级属性。

### 示例 2：从所有可见的网络适配器中获取所有高级属性
```
PS C:\> Get-NetAdapterAdvancedProperty -Name "*" -AllProperties
```

这个命令会获取所有可见网络适配器的所有高级属性。

### 示例 3：从所有可见的网络中获取所有的注册表属性
```
PS C:\> Get-NetAdapterAdvancedProperty -Name "*" -RegistryKeyword "*"
```

这个命令会获取所有可见网络适配器的全部注册表属性。

### 示例 4：从隐藏和可见的网络适配器中获取所有高级属性
```
PS C:\> Get-NetAdapterAdvancedProperty -Name "*" -AllProperties -IncludeHidden
```

这个命令可以获取所有可见和隐藏的网络适配器的所有高级属性信息。

### 示例 5：获取所有网络适配器的所有高级属性
```
PS C:\> Get-NetAdapterAdvancedProperty -Name "*" -RegistryKeyword "*" -IncludeHidden
```

这个命令可以获取所有网络适配器的所有高级属性。

### 示例 6：从指定的网络适配器中获取所有未格式化的高级属性
```
PS C:\> Get-NetAdapterAdvancedProperty -Name "MyAdapter" | Format-List -Property "*"
```

这个命令会获取名为“MyAdapter”的网络适配器上的所有未格式化的、高级属性信息。

### 示例 7：使用显示名称作为搜索字符串来获取网络适配器的高级属性
```
PS C:\> Get-NetAdapterAdvancedProperty -Name "*" | Where-Object -FilterScript { $_.DisplayName -Like "TCP*" }
```

这个命令用于获取那些显示名称以“TCP”开头的网络适配器的高级属性。

## 参数

### -AllProperties
表示该cmdlet会获取网络适配器的所有高级属性。如果未指定此参数，则仅返回具有“DisplayName”属性的高级属性。

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

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job` cmdlets系列。要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisplayName
指定高级属性的名称（以数组形式表示），这些属性会在 Windows Server® 2012 及更高版本中网络适配器属性下的“高级”选项卡中显示。

```yaml
Type: String[]
Parameter Sets: ByNameDisplayName, ByInstanceIDDisplayName
Aliases: DispN

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IncludeHidden
该参数表示此 cmdlet 在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了该参数，则该通配符字符串会将隐藏网络适配器和可见网络适配器都包含在内。

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

### -InterfaceDescription
指定一个网络适配器接口描述数组。对于物理网络适配器来说，这通常是网络适配器的厂商名称后跟型号和描述，例如 `Contoso 12345 千兆网络设备`。

```yaml
Type: String[]
Parameter Sets: ByInstanceIDKeyword, ByInstanceIDDisplayName, ByInstanceID
Aliases: ifDesc, InstanceID

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个网络适配器名称数组。

```yaml
Type: String[]
Parameter Sets: ByName, ByNameRegistryKeyword, ByNameDisplayName
Aliases: ifAlias, InterfaceAlias

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -RegistryKeyword
指定此 cmdlet 读取的注册表值的名称，例如 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0007 中找到的某个注册表值。

```yaml
Type: String[]
Parameter Sets: ByNameRegistryKeyword, ByInstanceIDKeyword
Aliases: RegKey

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。这个限制仅适用于当前正在运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/MSFT_NetAdapterAdvancedPropertySettingData
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[New-NetAdapterAdvancedProperty](./New-NetAdapterAdvancedProperty.md)

[Remove-NetAdapterAdvancedProperty](./Remove-NetAdapterAdvancedProperty.md)

[Reset-NetAdapterAdvancedProperty](./Reset-NetAdapterAdvancedProperty.md)

[Set-NetAdapterAdvancedProperty](./Set-NetAdapterAdvancedProperty.md)

