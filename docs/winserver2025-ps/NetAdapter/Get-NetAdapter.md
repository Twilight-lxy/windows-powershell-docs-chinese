---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_NetAdapter.cmdletDefinition.cdxml-help.xml
Module Name: NetAdapter
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/netadapter/get-netadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-NetAdapter
---

# Get-NetAdapter

## 摘要
获取基本的网络适配器属性。

## 语法

### 按名称排序（默认方式）
```powershell
Get-NetAdapter [[-Name] <String[]>] [-IncludeHidden] [-Physical] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### ByInstanceID
```powershell
Get-NetAdapter -InterfaceDescription <String[]> [-IncludeHidden] [-Physical] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

### 作者：ByIfIndex
```powershell
Get-NetAdapter -InterfaceIndex <UInt32[]> [-IncludeHidden] [-Physical] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-NetAdapter` cmdlet 可以获取基本的网络适配器属性。默认情况下，仅返回可见的适配器信息。若要查看网络适配器的常用属性，可将输出结果传递给 `Format-List` cmdlet；若要查看所有属性，则需将输出结果传递给 `Format-List` cmdlet，并将 `Property` 参数设置为通配符 “*”。该 cmdlet 支持多种显示方式：默认显示方式为表格形式。若想了解有关网络适配器标识符的更多信息，可使用 `Format-Table` cmdlet 并将 `View` 参数设置为 “names”；若想了解有关迷你端口或设备驱动程序（如驱动程序的版本等信息），则可使用 `Format-Table` cmdlet 并将 `View` 参数设置为 “driver”。

## 示例

### 示例 1：获取所有可见的网络适配器
```powershell
PS C:\> Get-NetAdapter -Name *
```

这个命令可以获取所有可见的网络适配器。

### 示例 2：获取所有可见和隐藏的网络适配器
```powershell
PS C:\> Get-NetAdapter -Name * -IncludeHidden
```

这个命令可以获取所有的网络适配器信息。

### 示例 3：获取所有的物理网络适配器
```powershell
PS C:\> Get-NetAdapter -Name * -Physical
```

这个命令可以获取所有的物理网络适配器。

### 示例 4：根据指定的名称获取网络适配器
```powershell
PS C:\> Get-NetAdapter -Name "Ethernet 2"
```

这个命令用于获取名为“Ethernet 2”的网络适配器。

### 示例 5：通过指定的名称获取网络适配器
```powershell
PS C:\> Get-NetAdapter -Name "E*2"
```

这个命令使用通配符来获取以“E”开头、以“2”结尾的适配器。

### 示例 6：显示指定网络适配器的常见属性
```powershell
PS C:\> Get-NetAdapter -Name "Ethernet 3" | Format-List -Property *
```

此命令显示名为“Ethernet 3”的网络适配器的常见属性，并使用**Format-List** cmdlet对列表进行格式化处理。

### 示例 7：显示指定网络适配器的所有属性
```powershell
PS C:\> Get-NetAdapter -Name "Ethernet 6" | Format-List -Property *
```

这个命令会显示名为“Ethernet 6”的网络适配器的所有属性信息。

### 示例 8：使用与前缀模式匹配的接口描述来获取所有网络适配器
```powershell
PS C:\> Get-NetAdapter -Name * -InterfaceDescription "VendorAdapter*"
```

这个命令会获取所有使用接口描述“VendorAdapter”（该描述符合前缀模式）的网络适配器。

### 示例 9：显示所有网络适配器的参数值
```powershell
PS C:\> Get-NetAdapter -Name "*" -IncludeHidden | Format-List -Property "Name", "InterfaceDescription", "InterfaceName"
```

此命令会显示所有网络适配器的*名称*、*接口描述*和*接口名称*参数值。

### 示例 10：获取指定服务器上可见的网络适配器
```powershell
PS C:\> Get-NetAdapter -Name * -CimSession "Server5"
```

这个命令用于获取名为 Server5 的服务器上可见的网络适配器信息。Server5 可以是一台远程计算机。

### 示例 11：获取可见的网络适配器并格式化输出结果
```powershell
PS C:\> Get-NetAdapter -Name * | Format-Table -View Driver
```

这个命令可以获取可见的网络适配器，并将输出结果格式化为便于查看驱动程序信息的形式。

### 示例 12：获取可见的网络适配器并格式化输出结果
```powershell
PS C:\> Get-NetAdapter -Name * | Format-Table -View Name
```

这个命令会获取可见的网络适配器，并将输出结果格式化为多种形式，以便显示网络适配器的各种标识信息，例如 *Name*（名称）、*InterfaceDescription*（接口描述）和 *InterfaceName*（接口名称）等参数值。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用 `-*Job` 系列 cmdlet；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关 Windows PowerShell® 后台作业的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者输入一个会话对象（例如 [New-CimSession](/powershell/module/cimcmdlets/new-cimsession) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中运行。

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

### -IncludeHidden
该参数表示此cmdlet在操作过程中会同时包含可见网络适配器和隐藏网络适配器。默认情况下，仅包含可见网络适配器。如果在识别网络适配器时使用了通配符，并且指定了此参数，则该通配符字符串将匹配所有隐藏和可见的网络适配器。

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
指定一个网络适配器接口描述的数组。对于物理网络适配器来说，这通常是网络适配器供应商的名称后跟部件编号和描述，例如“Contoso 12345 千兆网络设备”。

```yaml
Type: String[]
Parameter Sets: ByInstanceID
Aliases: ifDesc

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InterfaceIndex
以数组的形式指定网络适配器接口的索引编号。

```yaml
Type: UInt32[]
Parameter Sets: ByIfIndex
Aliases: ifIndex

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
指定一个网络适配器名称数组。

```yaml
Type: String[]
Parameter Sets: ByName
Aliases: ifAlias, InterfaceAlias

Required: False
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Physical
表示该 cmdlet 会获取所有的物理网络适配器。

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

### -ThrottleLimit
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或整个计算机。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#ROOT/StandardCimv2/NetAdapter
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

[CIM_NetworkAdapter 类](/windows/win32/cimwin32prov/cim-networkadapter)

## 备注

## 相关链接

[Disable-NetAdapter](./ Disable-NetAdapter.md)

[Enable-NetAdapter](./Enable-NetAdapter.md)

[ Rename-NetAdapter](./Rename-NetAdapter.md)

[重启网络适配器](./Restart-NetAdapter.md)

[Set-NetAdapter](./Set-NetAdapter.md)
